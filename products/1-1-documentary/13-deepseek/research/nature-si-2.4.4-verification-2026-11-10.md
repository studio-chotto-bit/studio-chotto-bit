# Nature 補足資料 §2.4.4 原表の直接確認（2026-11-10）

DeepSeek（1-1-13）の DeepReview Major 2件のうち1件、および裏取りR2の判定欄に残っていた
「最終確認の宿題」＝ Nature 補足資料 §2.4.4 の原表の直接確認を、2026-11-10 19:32 JST（10:32 UTC）に
原資料の PDF 本文で直接確認した。結果：**原稿の数字はすべて原表と一致**。

## 確認した原資料

- 論文：Guo et al.「DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning」、
  Nature 645, 633–638 (2025)
- 補足資料 PDF：https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-025-09422-z/MediaObjects/41586_2025_9422_MOESM1_ESM.pdf
- 該当箇所：§2.4.4 Training Cost（p.26）および Supplementary Table 4（p.27）

## 原文（抜粋・原文ママ）

§2.4.4 本文：

> For the training of DeepSeek-R1-Zero, we employed 64*8 H800 GPUs, and the process
> required approximately 198 hours. Additionally, during the training phase of DeepSeek-R1,
> we utilized the same 64*8 H800 GPUs, completing the process in about 4 days, or roughly
> 80 hours. To create the SFT datasets, we use 5K GPU hours.

Supplementary Table 4 キャプション：

> Training costs of DeepSeek-R1, assuming the rental price of H800 is $2 per GPU hour.

Supplementary Table 4（行：DeepSeek-R1-Zero / SFT data creation / DeepSeek-R1 / Total）：

> in H800 GPU Hours — 101K / 5K / 41K / 147K
> in USD — $202K / $10K / $82K / $294K

## 原稿との照合（manuscript/3.md L23–25）

| 項目 | 原稿 | 原表 | 判定 |
|---|---|---|---|
| R1-Zero の強化学習 | 10万1,000 GPU時間（20万2,000ドル） | 101K GPU時間／$202K | 一致 |
| 教師データ作成 | 5,000 GPU時間（1万ドル） | 5K GPU時間／$10K | 一致 |
| 最終版 R1 の強化学習 | 4万1,000 GPU時間（8万2,000ドル） | 41K GPU時間／$82K | 一致 |
| 合計 | 14万7,000 GPU時間、29万4,000ドル | 147K／$294K | 一致 |
| 計算機 | H800 を 512基 | 64×8 H800 GPUs（＝512基） | 一致 |
| 実時間 | R1-Zero 約198時間、R1 約80時間 | 約198時間／約80時間（"about 4 days, or roughly 80 hours"） | 一致 |

検算も整合：101K ÷ 512 ≒ 197時間（≒198時間）、41K ÷ 512 ≒ 80時間。
「約278時間」は 198＋80 の合計で、段階ごとの時間は上記のとおり。
二次ソースにあった「648基」は原表の 64×8（512基）と矛盾するため誤記で確定。

## 最終確認への申し送り（要対応1件）

ブラッシュアップ（2026-11-10）で読者向けの留保として書き換えられた次の文言は、
本確認により**前提が変わった**ため、最終確認で更新すること。

- 対象：`manuscript/paid.md:120`（確度一覧・台帳の注記）
- 現行文言：「R1系の学習コスト29万4,000ドルの内訳（Nature掲載版の補足資料のコスト表に
  基づく数字で、複数のソースが一致している。ただし補足資料の原表そのものは、本稿の執筆時点で
  直接確認できていない）」
- 対応案：括弧内を「Nature掲載版の補足資料 §2.4.4・Supplementary Table 4 の原表で直接確認済み」
  趣旨に書き換える。数字そのものの修正は不要（すべて一致）。
- 判定の扱い：裏取りR2の「独立確認あり（数値は二次ソースの一致による）」は、
  本確認により「**一次資料（原表）で直接確認**」へ格上げできる。

## 原稿への反映（2026-11-10 実施済み）

Akira の「進めて」を受け、上記の対応を実施した。

- `manuscript/paid.md` の「数字の確度一覧」から、旧文言（「直接確認できていない」）の項目を削除。
- 同項目を「一次資料で確認」へ移し、文言を「R1系の学習コスト29万4,000ドルの内訳（Nature掲載版の補足資料 §2.4.4 と Supplementary Table 4 の原表で直接確認）」へ更新。
- 数字そのものの修正はなし（すべて原表と一致）。repo 同期・照合は本記録とあわせて実施。

## 残件（本確認では変わらないもの）

- DeepSeek の残件はテーマ画像 → 最終確認 → note 下書き。公開は 2027-01-25・27・29。
- Genie（1-1-11）・サカナAI（1-1-12）の DeepReview は引き続き枠の回復待ち（dev01 の今週枠は使い切り）。
