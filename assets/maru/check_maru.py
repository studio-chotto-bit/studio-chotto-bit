#!/usr/bin/env python3
"""まる（CHOTTO BIT 共通キャラクター）の造形検品スクリプト。

使い方:
    python3 check_maru.py <image> [--region x,y,w,h]

- スタンドアロンの まる PNG（透過あり）: 顔の bbox はアルファ（>=128）の bbox。
- --region 指定時: その矩形を顔の bbox として使う（合成シーン等の検品用）。
- どちらも無い場合: 画像全体を顔の bbox とする。

測定:
- 顔 bbox 内で暗色ブロブ（max(R,G,B) < 110）を連結成分として抽出し、
  近接する成分を1つのブロブにまとめる（「考える」の点々目対応）。
- 縦 25〜65% の帯域にあるブロブから、左右ペア（y 中心差が最小の組）を目として選ぶ。
- 目の間隔比 =（右目の左端 − 左目の右端）/ 顔幅 … いわゆる「内縁間距離」。
  参考値として中心間距離も出力する。

合格条件: 目が2つ検出され、かつ目の間隔比（内縁）が 0.20〜0.32 の範囲内。
終了コード: 合格 0 / 不合格 1。
"""
import argparse
import sys
from collections import deque

import numpy as np
from PIL import Image

DARK_MAX = 110          # これ未満の max(R,G,B) を「暗色」とみなす
ALPHA_MIN = 128         # 顔として扱うアルファの下限
EYE_BAND = (0.25, 0.65) # 目の探索帯域（顔の高さ比）
MOUTH_BAND = (0.55, 0.85)
PAIR_CY_TOL = 0.12      # 目ペアの y 中心差の許容（回転ポーズ対応）
GAP_MIN, GAP_MAX = 0.20, 0.32


def label_components(mask):
    """8近傍の連結成分を返す。"""
    pts = set(map(tuple, np.argwhere(mask).tolist()))
    comps = []
    while pts:
        seed = pts.pop()
        q = deque([seed])
        members = [seed]
        while q:
            y, x = q.popleft()
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    nb = (y + dy, x + dx)
                    if nb in pts:
                        pts.discard(nb)
                        q.append(nb)
                        members.append(nb)
        arr = np.array(members)
        comps.append((arr[:, 0], arr[:, 1]))
    return comps


def analyze(rgb, bbox):
    """rgb: HxWx3 配列（白背景に合成済み）, bbox=(x0,y0,x1,y1) inclusive。
    測定値の dict を返す。"""
    x0, y0, x1, y1 = bbox
    W = x1 - x0 + 1
    H = y1 - y0 + 1
    region = rgb[y0:y1 + 1, x0:x1 + 1].astype(int)
    dark = region.max(axis=2) < DARK_MAX
    min_area = max(2, int(0.0002 * W * H))
    blobs = []
    for ys, xs in label_components(dark):
        if len(xs) < min_area:
            continue
        blobs.append(dict(cx=float(xs.mean()), cy=float(ys.mean()),
                          x_min=int(xs.min()), x_max=int(xs.max()),
                          y_min=int(ys.min()), y_max=int(ys.max()), n=len(xs)))
    # 近接成分をクラスタリング（点々目を1つの目としてまとめる）
    blobs.sort(key=lambda b: b['cx'])
    clusters = []
    for b in blobs:
        placed = False
        for cl in clusters:
            ccx = np.mean([m['cx'] for m in cl])
            ccy = np.mean([m['cy'] for m in cl])
            if abs(b['cx'] - ccx) < 0.08 * W and abs(b['cy'] - ccy) < 0.08 * H:
                cl.append(b)
                placed = True
                break
        if not placed:
            clusters.append([b])
    groups = []
    for cl in clusters:
        n = sum(m['n'] for m in cl)
        groups.append(dict(
            cx=sum(m['cx'] * m['n'] for m in cl) / n,
            cy=sum(m['cy'] * m['n'] for m in cl) / n,
            x_min=min(m['x_min'] for m in cl), x_max=max(m['x_max'] for m in cl),
            y_min=min(m['y_min'] for m in cl), y_max=max(m['y_max'] for m in cl),
            parts=len(cl)))
    for g in groups:
        g['w'] = g['x_max'] - g['x_min'] + 1
        g['h'] = g['y_max'] - g['y_min'] + 1

    band = [g for g in groups
            if EYE_BAND[0] * H <= g['cy'] <= EYE_BAND[1] * H and g['w'] <= 0.26 * W]
    best = None
    for i in range(len(band)):
        for j in range(i + 1, len(band)):
            L, R = band[i], band[j]
            if R['cx'] < L['cx']:
                L, R = R, L
            if abs(L['cy'] - R['cy']) < PAIR_CY_TOL * H and L['cx'] < 0.52 * W and R['cx'] > 0.48 * W:
                score = abs(L['cy'] - R['cy'])
                if best is None or score < best[0]:
                    best = (score, L, R)
    res = {'face_w': W, 'face_h': H}
    if best is None:
        res['eyes_found'] = 0
        return res
    _, L, R = best
    res['eyes_found'] = 2
    res['eye_left'] = (L['cx'] / W, L['cy'] / H)
    res['eye_right'] = (R['cx'] / W, R['cy'] / H)
    res['eye_spacing_center'] = (R['cx'] - L['cx']) / W
    res['eye_spacing_gap'] = (R['x_min'] - L['x_max']) / W
    res['eye_width_ratio'] = ((L['w'] + R['w']) / 2) / W
    rest = [g for g in groups if g is not L and g is not R
            and MOUTH_BAND[0] * H <= g['cy'] <= MOUTH_BAND[1] * H]
    if rest:
        mcx = np.mean([g['cx'] for g in rest])
        mcy = np.mean([g['cy'] for g in rest])
        mw = max(g['x_max'] for g in rest) - min(g['x_min'] for g in rest) + 1
        res['mouth'] = (mcx / W, mcy / H)
        res['mouth_width_ratio'] = mw / W
    return res


def main():
    ap = argparse.ArgumentParser(description='まる造形検品')
    ap.add_argument('image')
    ap.add_argument('--region', help='顔の矩形 x,y,w,h（画像座標）')
    args = ap.parse_args()

    im = Image.open(args.image).convert('RGBA')
    alpha = np.asarray(im)[..., 3]
    bg = Image.new('RGBA', im.size, (255, 255, 255, 255))
    rgb = np.asarray(Image.alpha_composite(bg, im).convert('RGB'))

    if args.region:
        x, y, w, h = (int(v) for v in args.region.split(','))
        bbox = (x, y, x + w - 1, y + h - 1)
        src = f'region {args.region}'
    elif (alpha < 255).any():
        ys, xs = np.where(alpha >= ALPHA_MIN)
        if len(xs) == 0:
            print('FAIL: 顔が見つかりません（アルファが空）')
            return 1
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max()))
        src = 'alpha bbox'
    else:
        bbox = (0, 0, im.width - 1, im.height - 1)
        src = 'whole image'

    r = analyze(rgb, bbox)
    print(f"file: {args.image}")
    print(f"face bbox ({src}): x={bbox[0]} y={bbox[1]} w={r['face_w']} h={r['face_h']}")
    if r.get('eyes_found') != 2:
        print('eyes: 検出できませんでした')
        print('RESULT: FAIL')
        return 1
    print(f"eye left center : x/W={r['eye_left'][0]:.3f} y/H={r['eye_left'][1]:.3f}")
    print(f"eye right center: x/W={r['eye_right'][0]:.3f} y/H={r['eye_right'][1]:.3f}")
    print(f"eye spacing (gap, inner edges): {r['eye_spacing_gap']:.3f}  [合格範囲 {GAP_MIN:.2f}〜{GAP_MAX:.2f}]")
    print(f"eye spacing (center to center): {r['eye_spacing_center']:.3f}")
    print(f"eye width ratio : {r['eye_width_ratio']:.3f}")
    if 'mouth' in r:
        print(f"mouth center    : x/W={r['mouth'][0]:.3f} y/H={r['mouth'][1]:.3f}  width ratio {r['mouth_width_ratio']:.3f}")
    ok = GAP_MIN <= r['eye_spacing_gap'] <= GAP_MAX
    print('RESULT:', 'PASS' if ok else 'FAIL')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
