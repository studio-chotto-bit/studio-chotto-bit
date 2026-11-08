# P36 DeepReview レポート（2026-11-08）

- 対象：P36『「黄金のルート」』統合原稿（p36-combined-0-1.md、無料部＋有料部）
- 使用アカウント：事業用サブ（accdisc.01.01@gmail.com、専用プロファイル）
- 結果ページ：https://research.google/deepreview/documents/1f38074d-b959-43dd-9f74-370969d67ab2
- 指摘：全12件（Major 1／Minor 7／Suggestion 4）
- 総評：歴史再構成（2007年 Macworld 基調講演、Gorilla Glass への6か月の移行）は正確で、誤解の訂正（1962年 Chemcor と2007年の新配合の区別、スコッチは客席で飲んだ点）も評価された。指摘は架空事例・点検票サンプル側の内部整合が中心。
- 枠：accdisc は前日（11/7）の P38 2回目で今週1件使用済みだったため、本件が2件目として枠内で受理された。

## Overall Feedback

### Summary

This document analyzes the January 9, 2007 first-generation iPhone keynote demonstration and the subsequent six-month manufacturing sprint to commercial launch, synthesizing primary journalistic testimonies and biographical records to examine how an unstable prototype was successfully demonstrated live. Drawing on this historical analysis—including the scripted "Golden Path" operational sequence, backstage hardware and wireless redundancies, and the rapid transition from plastic to Corning Gorilla Glass—the author proposes a practical six-step operational design and risk-governance framework (Steps 0 through 5) for staging live demonstrations of unfinished products. The document complements this methodology with a fictional B2B case study, a copy-ready pre-demo inspection worksheet gated by empirical verification criteria, and a completed sample checklist.

### Strengths

- The document offers a cross-disciplinary synthesis that bridges front-stage operational constraint engineering (Steps 1–4) with a pre-demo Go/No-Go governance gate tied to a post-announcement completion schedule (Step 0) and an explicit ethical audit separating acceptable staging from audience deception (Step 5).
- The historical reconstruction of the 2007 Macworld keynote and the six-month Corning Gorilla Glass transition is well-researched and accurate, carefully correcting common misconceptions (such as distinguishing 1962 Chemcor from the newly formulated 2007 Gorilla Glass and clarifying that engineers drank scotch in the audience rather than backstage).
- The operationalized inspection worksheet (点検票) provides high practical utility for engineering, product, and sales teams by requiring empirical verification (未着手／要検証／確認済み backed by rehearsal metrics or test logs) and explicitly incorporating fault-injection rehearsals and abort criteria.

### Weaknesses

- The fictional walkthrough (通し実例) and completed worksheet sample (記入済みサンプル) contain internal logical and cross-artifact inconsistencies: most notably, despite locking down a strict 12-minute recording as the "Golden Path" in Step 2 to avoid the ~40-minute crash threshold identified in Step 1, the narrative states that the live demo crashed a second time while processing "long audio" (長い音声の処理), alongside minor mismatches in demonstrated feature scope, primary versus backup network terminology, an unresolved 要検証 room-reverberation item, and a missing Step 0 damage estimate.
- While the six-step framework provides a valuable integrated synthesis for practitioners, its individual components closely mirror established methodologies in product governance, software risk management, site reliability engineering, sales engineering, and technology sociology, and the document might be further enriched by contextualizing its guidance within these foundational frameworks (Reference Paper: Stage-Gate Systems, Robert G. Cooper, 1990; Software Risk Management, Barry W. Boehm, 1991; Engineering a Safer World, Nancy G. Leveson, 2011; Site Reliability Engineering, Beyer et al., 2016; Great Demo!, Peter E. Cohan, 2005; The Demonstration Society, Claude Rosental, 2021; Vaporware, Suddenware, and Trueware, Ofek and Turut, 2013).
- In the blank inspection worksheet, the field label 担当者と期限／中止条件 is repeated identically across Steps 1 through 5, which blurs the distinction between step-specific operational role owners (担当), pre-demo task deadlines, and live-demo abort criteria (中止条件), while Step 3 omits a prompt for aligning responses to questions about unshown features.
- Minor structural and editorial issues slightly affect the narrative flow, including mentioning memory exhaustion in the L0037 summary before it is formally introduced in L0054, a duplicated level-1 title header at L0048, and inconsistent script usage for Wendell Weeks (ウィークス vs. Weeks).

## Detailed Feedback（12件）

### Suggestion／Line 1／タイトルの二重括弧

In the title # 『「黄金のルート」』——初代iPhone発表デモと、本番の設計, double corner brackets (『』) and single corner brackets (「」) are nested directly together. Unless this is an intentional stylistic choice, consider simplifying 『黄金のルート』 or 「黄金のルート」.
（提案）# 「黄金のルート」——初代iPhone発表デモと、本番の設計
（注記：『「…」』は有料ラインの決定タイトル様式＝P37『「コード・レッド」』と同形式のため、ブラッシュアップでは原則見送り候補）

### Suggestion／Line 17／「だが、」の連続

Two consecutive sections use the same conjunction (だが、会場の多くは気付かなかった。 in L0015 and だが、この日ステージで動いていた iPhone は、 in L0017). Varying or omitting the second だが、 would improve the transition between paragraphs.
（提案）この日ステージで動いていた iPhone は、完成品ではなかった。

### Minor／Line 37／未紹介のメモリ不足が要約に先行

Line 37 opens with a summary of the preceding section (整理しよう。この日の iPhone は、操作の順序を誤ると不具合が起き、タスクを重ねるとメモリ不足で再起動が必要になり、電波の表示は作り物だった。). However, the issue of memory exhaustion requiring a device reboot after performing multiple tasks has not yet been mentioned in Lines 1–34 (the reboot mentioned in L0031 refers specifically to the wireless radios crashing and restarting). Instead, the memory issue is introduced later in L0054 as a new point. To maintain logical progression, consider either briefly mentioning memory exhaustion alongside the other instabilities in L0023–L0030, or adjusting the summary in L0037 to reflect only the facts already presented up to that point.
（提案される要約文）整理しよう。この日の iPhone は、操作の順序を誤ると不具合が起き、曲や動画は最後まで安定して再生できず、電波の表示は作り物だった。

### Minor／Line 48／重複見出し（連結アーティファクト）

The main level-1 document heading from L0001 is repeated verbatim mid-article between the transitional paragraph at L0047 and the section heading at L0050 (## 見えない仕掛けの、残り). This appears to be a manuscript concatenation artifact and should be removed.
（注記：P35 と同様、統合ファイル側でのみ除去する）

### Suggestion／Lines 74–76／Weeks の表記統一

Corning CEO Wendell Weeks is introduced in katakana (ウェンデル・ウィークス) in L0070, but subsequent references switch to Latin script (Weeks in L0074, L0076, L0078, L0094, and L0098), whereas other individuals in the text (ジョブズ, グリニョン, ジョン・シーリー・ブラウン) are consistently written in katakana. Consider standardizing to ウィークス throughout for editorial consistency.

### Suggestion／Line 126／先行手法への位置づけ

While the six-step framework provides a valuable integrated synthesis for practitioners, its individual components closely mirror established methodologies in product governance, software risk management, site reliability engineering, sales engineering, and technology sociology. The document could be further enriched by contextualizing its guidance within these foundational frameworks—such as stage-gate product governance (Cooper, 1990), software risk management (Boehm, 1991), systems-theoretic safety constraints (Leveson, 2011), site reliability engineering practices (Beyer et al., 2016), structured software demonstration design (Cohan, 2005), the sociology of public technology demonstrations (Rosental, 2021), and product preannouncement dynamics (Ofek and Turut, 2013).

### Major／Line 198／12分の固定手順と「長い音声」での2回目の停止の矛盾

There is an internal logical contradiction between how Company S designs its "Golden Path" in Step 2 (L0190, L0264) and the live demo's second failure in L0198:
- In Step 1 (L0188, L0263), the team identifies two failure conditions: (1) processing crashes when audio length exceeds approximately 40 minutes, and (2) proper-noun recognition degrades in reverberant rooms.
- In Step 2 (L0190, L0264), to avoid the 40-minute crash threshold, the team strictly locks the live procedure to playing a single 12-minute pre-recorded internal meeting and forbids any other operations, allowing deviation only upon M's pre-agreed failover signal.
- In Step 4 (L0194), the fallback plan when a stall occurs is to restart the same sequence using an even shorter audio clip, which is executed after the first stall in L0198.
- However, L0198 then states that toward the end of the session, the system stalled a second time while processing a "long audio" (しかし終盤、長い音声の処理でもう一度止まり、復旧にも時間がかかった), immediately before L0202 concludes that the failure occurred inside the assembled safe conditions.
Under the rules locked in Step 2 and Step 4, processing a "long audio" should never occur during the 45-minute meeting unless someone violated Step 2 by improvising—which would contradict L0202's conclusion that the failure happened inside the designed conditions. Revising L0198 so that the second stall occurs within the locked 12-minute or fallback workflow would resolve this contradiction.
（提案される修正文）しかし終盤、元の12分の音声に戻して要約と決定事項の抽出を進めたところでもう一度止まり、復旧にも時間がかかった。

### Minor／Lines 236–238／点検票の「担当者と期限／中止条件」の混同と Step 3 の設問不足

In the blank inspection worksheet (L0204–L0259), Steps 1 through 5 all repeat the exact same line: - 担当者と期限／中止条件：（　　　　　　）. In the prose methodology (L0128–L0180), "abort conditions" (中止条件) belong specifically to Step 0 (L0132) and Step 4 (L0168), whereas Steps 1–5 each define specific operational role owners (担当: L0144; L0153; L0162; L0171; L0180) rather than step-level abort conditions. Noticeably, the completed sample (L0262–L0267) omits this repeated field in Steps 1, 2, 4, and 5. Repeating ／中止条件 across every step blurs the distinction between the owner/deadline for pre-demo preparation tasks, the step's operational owner, and live-demo abort criteria.
Additionally, while the prose in Step 3 (L0159), the case study (L0192), and the completed sample (L0265) all emphasize preparing aligned answers when asked about unshown/in-development features, the Step 3 worksheet (L0233–L0239) lacks a prompt for this item.
Replace the repetitive field in Steps 1–5 with the specific role owner defined for each step alongside an optional field for open-task deadlines (e.g., - 担当者（残件がある場合はその期限）：), keeping abort conditions in Step 0 and Step 4 where they are defined, and add a prompt in Step 3 for how to answer questions about unshown or in-development features.
（提案される Step 3 の設問）
- 開発中の機能／確認済みの性能／未検証の性能の切り分けと、進捗を聞かれたときの答え方：（　　　　　　）
- 確認の根拠：（　　　　　　）
- 担当者（見せる範囲・対外文面の決定者、および残件の期限）：（　　　　　　）

### Minor／Line 253／Step 5 の書式不統一

In Steps 0–4 of the blank worksheet, all individual check items use fill-in blanks （　　　　　　） and the 3-level status rating (未着手／要検証／確認済み) appears once at the end of each step. In Step 5, however, L0253 uses 未着手／要検証／確認済み mid-list, resulting in two separate rating lines in Step 5 (L0253 and L0258). Changing L0253 to use （　　　　　　） (leaving L0258 as the step's summary rating) would keep the worksheet structure uniform across all steps.
（提案される修正後の L0253）- 発売・納品時の姿と矛盾する期待を作っていないか：（　　　　　　）

### Minor／Line 262／Step 0 の損害見積もりが事例とサンプルに欠落

Step 0 of the prose methodology (L0132(b)) and the blank worksheet (L0211: - 誤作動による損害の見積もり) require estimating potential damages from malfunction, and L0133 stipulates that if even one of the five items is ambiguous, the team must not proceed. However, neither the case study narrative (L0188) nor Step 0 of the completed sample (L0262) includes this damage estimate. Include a brief entry for 誤作動による損害の見積もり in both L0188 and L0262.
（提案される Step 0 の記入例）- ステップ0：続行条件＝12分の録音で全工程が3回連続で完走すること。中止条件＝処理が2回止まる、または復旧に3分以上かかること。損害の見積もり＝自社録音のみ使用のため顧客情報の流出はないが、固有名詞の誤変換を放置すると精度への誤認を招く。完成期限＝2か月後に検証済みの範囲から段階提供。決定者＝K：確認済み（根拠：リハーサル3回の完走記録）。

### Minor／Line 265／反響条件の「要検証」の扱いと、見せる範囲の不一致

In L0188 and L0263, proper-noun recognition errors in reverberant rooms are identified as one of two failure conditions in Step 1, yet the prose narrative (L0190–L0197) never explains how this second condition was addressed before the live demo. Meanwhile, Step 3 of the completed sample (L0265) marks this item as 要検証 with an open task due by the day before the demo, while all other steps are marked 確認済み. First, because Step 2 plays a pre-recorded 12-minute audio file rather than capturing live microphone input in the client's room, it is unclear why the acoustics of the demo venue would affect the fixed demo path. Second, the narrative proceeds to the live demo in L0198 without explaining how this 要検証 item was resolved prior to going live. Clarify in L0190–L0192 and L0265 how the reverberation risk was handled.
Discrepancy in demonstrated features: Both the case study narrative (L0190) and Step 2 of the completed sample (L0264) define the fixed demonstration sequence as covering transcription, summarization, and decision extraction. However, Step 3 of the completed sample (L0265) states that what is shown goes only up to transcription and summarization, omitting 決定事項の抽出. Align L0265 to include 決定事項の抽出.
（提案される修正：反響の扱い）ただし、反響の強い部屋での固有名詞の精度は未検証のため「未検証の性能」として切り分け、聞かれたら検証中と説明する：要検証（残件：反響の強い会議室での実測値をデモ前日までに測定する。担当は M）。
（提案される修正：Step 3 の見せる範囲）- ステップ3：見せるのは日本語会議の文字起こし・要約・決定事項の抽出まで。

### Minor／Line 266／主回線／予備回線の用語不一致

In L0194, Company S sets its own mobile router as the primary connection instead of the venue's Wi-Fi, and in L0198 they switch to a "backup line" (予備回線に切り替え) when the mid-demo stall occurs. In contrast, L0266 (Step 4) describes the partial-failure fallback as switching to the self-provided line (部分の失敗＝予備 PC と自前回線へ切替), implying the self-provided line was the backup rather than the primary connection. Make the primary/backup network terminology consistent across L0194, L0198, and L0266.
（提案される修正後の Step 4）- ステップ4：部分の失敗＝予備 PC と別キャリアの予備回線へ切替、繋ぎは営業担当が説明を継続。
