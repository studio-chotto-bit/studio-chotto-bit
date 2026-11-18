import math, sys, os
from PIL import Image, ImageDraw, ImageFilter

BASE = '/home/hatch/workspace/goals/paid-note-article-preparation/maru-motion-test'
W = H = 1080; FPS = 30; N = 90
BG = (246, 241, 231, 255)
SIZE = 620; GROUND_Y = 880; CX = W // 2

def ease_out(p): return 1 - (1 - p) ** 3

def pose(t):
    if t < 0.9:
        return 5 * (1 - math.cos(2 * math.pi * t / 0.9)) / 2, 1.5 * math.sin(2 * math.pi * t / 0.9), 1.0
    if t < 1.5:
        p = (t - 0.9) / 0.6
        return 130 * math.sin(math.pi * p), 6 * math.sin(math.pi * p), 1 - 0.35 * math.sin(math.pi * p)
    if t < 2.1:
        p = ((t - 1.5) % 0.3) / 0.3
        return 34 * math.sin(math.pi * p), 3 * math.sin(2 * math.pi * (t - 1.5) / 0.6), 1 - 0.12 * math.sin(math.pi * p)
    p = (t - 2.1) / 0.9
    return (1 - ease_out(p)) * 6 + 3 * (1 - math.cos(2 * math.pi * (t - 2.1) / 0.9)) / 2 * ease_out(p), (1 - ease_out(p)) * 2 * math.sin(2 * math.pi * (t - 2.1) / 0.45), 1.0

def render(src, tag):
    maru0 = Image.open(src).convert('RGBA').resize((SIZE, SIZE), Image.LANCZOS)
    d_rgba = f'{BASE}/frames-{tag}-rgba'; d_prev = f'{BASE}/frames-{tag}-prev'
    os.makedirs(d_rgba, exist_ok=True); os.makedirs(d_prev, exist_ok=True)
    for i in range(N):
        t = i / FPS
        lift, roll, ss = pose(t)
        layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        sh_w, sh_h = int(430 * ss), int(56 * ss)
        shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(shadow).ellipse([CX - sh_w // 2, GROUND_Y + 18 - sh_h // 2, CX + sh_w // 2, GROUND_Y + 18 + sh_h // 2], fill=(90, 70, 50, int(70 * ss)))
        layer = Image.alpha_composite(layer, shadow.filter(ImageFilter.GaussianBlur(10)))
        m = maru0.rotate(-roll, resample=Image.BICUBIC, center=(SIZE // 2, SIZE // 2))
        layer.alpha_composite(m, (CX - SIZE // 2, int(GROUND_Y - SIZE - lift)))
        layer.save(f'{d_rgba}/{i:03d}.png')
        bg = Image.new('RGBA', (W, H), BG); bg = Image.alpha_composite(bg, layer)
        bg.convert('RGB').save(f'{d_prev}/{i:03d}.png')
    print('rendered', tag)

if __name__ == '__main__':
    render(sys.argv[1], sys.argv[2])
