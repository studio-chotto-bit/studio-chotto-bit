# 裏取りラウンド1：Gemini 4 Neon／Googleのリリース頻度転換（1-1-15）

- 実施日：2026-11-19
- 方法：公開ウェブの検索とページ本文取得。一次資料は Google 公式ブログ／DeepMind モデルカード／公式ドキュメントを優先し、報道は二次として扱った
- 判定の凡例：**一次資料で確認**／**独立確認あり**（複数の独立した情報源が一致）／**未確認・報道のみ**
- 前提（2026-11-19 追加指示）：公開まで約2週間半しかないため、本ラウンドは芯を支える数字（日付・価格・ベンチマーク・Argon 退場）を優先した。潰し切れなかった項目は末尾の「ラウンド2で潰す残件」に明確に切り分けた

## 項目1：Gemini 4系の発表日と順序／「7週間で4モデル」の正確性

- 主張：Argon 2026-09-30／Carbon 2026-10-28／Hydrogen 2026-11-12／Neon 2026-11-18 の順に発表され、「7週間で4モデル」「2カ月足らずで4つ目」と言える
- 確認できた事実：
  - Argon：2026-09-30 に Fairwind 向け限定で発表。モデルカードは 10/13 公開。一般提供（有料API）は 2026-10-13
  - Carbon：2026-10-28 に公式ポスト「Gemini 4 Carbon: our next frontier model」（Koray Kavukcuoglu 署名）で発表。当初は Fairwind のサイバー防御者サブセット向け。一般提供は 2026-11-10 の公式ポスト「Gemini 4 Carbon is now available」で開始
  - Hydrogen：2026-11-12 に公式ポストで発表
  - Neon：2026-11-18 に公式ポスト「Introducing Gemini 4 Neon」（Koray 署名）で発表
  - 9/30→11/18 は49日＝ちょうど7週間。Artificial Analysis も "its fourth model in just seven weeks" と明記。ITmedia の「2カ月足らずで4つ目」もこの範囲で正確
- 判定：**一次資料で確認**（発表日・順序・7週間の計算）
- 食い違い：Carbon について、一部の二次情報は一般提供日（11/10）を発表日と混同する。発表は 10/28、一般提供は 11/10 と書き分ける。Argon の一般提供を 10/14 とする二次情報もあるが、公式／API changelog ベースでは 10/13
- 出典：Google 公式ブログ（各発表ポスト）、DeepMind モデルカード、Artificial Analysis、ITmedia、9to5Google

## 項目2：Neon の位置づけと仕様

- 主張：Neon は Carbon 由来で、Carbon と Hydrogen の中間に位置し、100万トークンコンテキスト、思考レベル複数段階を持ち、発表当日に広く展開された
- 確認できた事実：
  - 公式ブログの「Where Neon sits in the Gemini 4 family」で、Carbon＝最も難しい長期プロジェクト、Hydrogen＝高速な日常実行、Neon＝その中間で深さと効率のバランス、と明記
  - モデルカードで「adapted from Gemini 4 Carbon（Carbon から適応）」。知識カットオフは 2026年3月（モデルカードを引く複数の二次情報で一致）
  - コンテキストは100万トークン（開発者ドキュメントでは入出力統合 1,048,576 トークン）
  - 思考レベルは4段階（low／medium／high が既定／xhigh）
  - 提供範囲（公式発表ポスト）：Gemini API（Google AI Studio）、Gemini for business（API とモデルドロップダウン）、Antigravity（Pro／Ultra）、Gemini アプリ（Pro／Ultra）。開発者向けには Android Studio も公式ポストの展開セクションに明記あり。API は有料枠のみ
  - Vertex AI への言及は公式発表ポストには無い
- 判定：**一次資料で確認**（位置づけ・提供範囲）。モデルカード原文の直接照合はラウンド2残件
- 食い違い・注意：Artificial Analysis は「Google's API and the Gemini Enterprise Agent Platform」経由で公開と書き、開発者ドキュメントは Gemini Enterprise Agent Platform 配下にある（旧 Vertex AI 系ドキュメントの移行先）。「Vertex AI」という名称での提供可否は、公式ドキュメントの直接確認をラウンド2で行う
- 出典：Google 公式ブログ（Neon 発表ポスト）、DeepMind モデルカード（二次引用経由）、開発者ドキュメント、Artificial Analysis

## 項目3：価格／12月1日の導入価格終了（第2のニュースフック）

- 主張：Neon は入力 $3／キャッシュ済み入力 $0.15／出力 $15（100万トークンあたり）。Carbon は標準価格 $4／$20、導入価格 $2／$10 が 2026-11-30 までで、12/1 から標準価格へ移る
- 確認できた事実：
  - Neon：入力 $3／キャッシュ済み入力 $0.15（95%引き）／出力 $15。公式ブログで確認
  - Carbon と Argon：標準価格は入力 $4／出力 $20。導入価格は入力 $2／出力 $10（キャッシュ $0.10）で **2026-11-30 まで**。**2026-12-01 から標準価格 $4／$20（キャッシュ $0.20）へ移行**する。公式価格表を引く複数の独立情報が一致
  - したがって Neon は Carbon の標準価格より25%安いが、11/30 までは導入価格の Carbon（$2/$10）より Neon の方が50%高いという逆転がある
  - **この 12/1 の価格改定は「第2のニュースフック」**：本命の公開日 2026-12-06（日）は改定の直後であり、「Neon 発表（11/18）」に続く出来事として記事の鮮度を支える。公開直前の鮮度チェックで改定が予定どおり実施されたか再確認する
- 判定：**独立確認あり**（Neon 価格は一次資料で確認。Carbon の価格改定は公式価格表を引く複数情報で一致。価格表原文の直接取得はラウンド2で補強する）
- 食い違い：aiweekly 等の一部二次情報が「Neon の $3/$15 も導入価格で 11/30 に失効する」と書いたが、これは Carbon／Argon の導入価格終了との混同とみられ、公式発表に Neon の期限の記載はない。未確認として原稿では使わない
- 出典：Google 公式ブログ（Neon 発表ポスト）、Google 公式価格表（二次引用経由）、複数の独立報道

## 項目4：ベンチマーク

- 主張：Neon は Artificial Analysis Intelligence Index で 61・総合3位、Coding Agent Index で首位級。タスク単価は競合より安い。「Carbon の3倍速・コスト約60%」という言い回しがある
- 確認できた事実：
  - Intelligence Index は Neon（xhigh）**61 で総合3位**（上位は GPT-6.2 Astra (max) と Claude Fable 5.2 (max)）。Carbon（high）60 を1点上回る
  - ただし Carbon は 10/28 発表時点では同 Index v5.0 で 59点・1位とされており、60 はその後の版（v5.0.1 等）／設定での値。版と設定の違いを原稿では明記する必要がある
  - Coding Agent Index は Google 公式発表値が **58.6（1位）**、Artificial Analysis 自身の記事では Antigravity CLI 実行で **59**（四捨五入表記）。Fable 5.2（xhigh、Claude Code）58 と同水準、Carbon（high）55
  - タスク単価は Coding Agent Index で Neon $6.86 に対し Fable 5.2 $15.47（半分以下）、Opus 5.5 $12.61。Intelligence Index 側では Neon $6.44 で Carbon $7.76（標準価格換算）より約17%安く、所要時間は約21分 vs 約36分（約40%短縮）、出力速度は約110 vs 約57 トークン/秒
  - Google 公式の言い回しは「既定の high 設定で Carbon よりタスク単価が **32%低い**」
  - **「Carbon の3倍速・コスト約60%」の起源は Google 自身のベンチマークではなく、パートナー企業 Glean の初期評価の証言（Thai Tran）**で、意味は「コストは Carbon の **60%**（＝40%安い）」
  - Google の19項目比較は比較対象が Opus 5.5 と GPT-6.2 Sol で、Neon が16項目で首位。Terminal-Bench 4.1 は 65.2% で Opus 5.5 の 65.8% を下回る
- 判定：**独立確認あり**（Artificial Analysis の数値）。Google 発表値と第三者評価は区別して書く
- 食い違い：「60% lower／60% cheaper」と書く報道が複数あるが、これは「コストが60%」の誤読。原稿では採用しない
- 出典：Artificial Analysis（Intelligence Index／Coding Agent Index の各記事）、Google 公式ブログ（Neon 発表ポスト）、SiliconANGLE 等の報道

## 項目5：Argon の退場

- 主張：Argon がモデル選択肢から消え、Neon が移行先とされた
- 確認できた事実：
  - **Gemini アプリでは退場を確認**（9to5Google 2026-11-18：Neon が Argon を置き換え、モデル選択は Auto／Everyday help＝Hydrogen／Deeper analysis＝Neon／Code & complex work＝Carbon の4つに再編。あわせて Gemini 3.1 Pro もアプリから退場）
  - ITmedia NEWS は「Argon は Google 公開の比較表にも開発者ドキュメントのモデル比較にも含まれず、Pro の選択項目からも消えた。Argon の今後の扱いについて Google は説明していない」と報道
  - ITmedia AI＋ は「Google は開発者向けドキュメントで、Argon を一般的なコーディングや推論に使っている場合の移行先に Neon を挙げている」と報道
  - 一方、開発者向け移行ガイド（Google Cloud ドキュメントのミラーで確認）では Argon は現行モデルとして残り、移行表では Argon の retirement date が「October 13, 2027 or later」とされ、Neon の開発者ガイドも「Argon からの移行」を扱う
- 判定：**独立確認あり**（アプリからの退場と Neon への移行誘導は事実）。**API の廃止告知は無い**
- 食い違い・注意：「Argon は消えた」とだけ書くと API 廃止と誤読される。原稿では「アプリからは退場、API では存続、公式の廃止告知なし」と書き分ける。開発者ドキュメント原文の直接確認はラウンド2残件
- 出典：9to5Google、ITmedia NEWS、ITmedia AI＋、Google Cloud ドキュメント（ミラー経由）

## 項目6：世代交代の旧リズム

- 主張：Gemini 1.0（2023-12-06）、1.5（2024-02-15）、2.0（2024-12-11）、2.5 Pro（2025-03-25）、3 Pro（2025-11-18）と、世代交代は年単位だった
- 確認できた事実：上記の各発表日が、年表系の複数情報と公式発表日で一致。1.5 は公式ブログ「Introducing Gemini 1.5」（Feb 15, 2024）で確認。Neon 発表の 2026-11-18 は Gemini 3 発表からちょうど1年
- 判定：**一次資料で確認／独立確認あり**
- 食い違い：特になし
- 出典：Google 公式ブログ、年表系の複数情報

## 項目7：2026年の加速の前段

- 主張：Flash 系が約3週間間隔で出るようになり、Gemini 3.5 Pro は約束されながら出荷されなかった
- 確認できた事実：
  - Flash 系は 3.6＝2026-07-21／3.7＝2026-08-13／3.8＝2026-09-02。間隔は23日と20日で、約3週間ごと。公式 changelog ベースの複数情報が一致
  - Gemini 3.5 Pro は 2026-05-19 の I/O で Pichai が「来月（6月）」と予告しながら未出荷。7月には Bloomberg が数カ月遅延・コーディング性能の未達を報道。8/5 に DeepMind の leadership 変更（Hassabis が会長／Alphabet chief scientist へ、Koray Kavukcuoglu が Gemini 開発を統括）。9/30 に Google スポークスパーソンが Reuters に「3.5 Pro は出さない」と確認し、Argon が後継に据えられた
- 判定：**独立確認あり**
- 食い違い：特になし（遅延の内情は報道ベースのため、原稿では報道として扱う）
- 出典：公式 changelog（二次経由）、Reuters、Bloomberg（二次経由）

## 項目8：経営層の発言

- 主張：ピチャイがリリースのリズム加速と、AI による開発加速の継続を語った
- 確認できた事実（一次ソースを2件特定）：
  - (a) **Sources ポッドキャスト**（Alex Heath 司会、2026-10-21 公開、YouTube https://www.youtube.com/watch?v=F3ItSTZNtT0）で Pichai は「今年は出す速度（cadence）を上げる必要があった。3.5→3.6→3.7→3.8 Flash で約3カ月にその連なりをやった。4.0 でも改善した cadence を期待する」趣旨を発言（書き起こしミラー ceointerviews.ai で文言確認）
  - (b) **Alphabet Q3 2026 決算（2026-10-28）の Pichai 発言は blog.google の公式 edited transcript で一次確認済み**：「We're at the point where AI is helping us increase our training and launch velocity. I would expect the next 12 months to see continued acceleration because of RSI.」（RSI の定義は発言内では展開されていない）
  - 追加で Reuters（2026-07-23、Q2 決算）は Pichai が Gemini 4 のロードマップについて「almost at a monthly cadence（ほぼ月次ペース）」と述べたと報道
- 判定：**一次資料で確認**（(a)(b) の趣旨）。ただし細部は下記の未確認を含む
- 未確認：「3.5 Pro would have had a very short shelf life（賞味期限が非常に短かっただろう）」という言い回しは ppc.land 等の二次要約経由で、原文の直接照合はラウンド2残件。**「リリースのリズム加速が最重要課題の一つ」という言い回し自体は一次資料で確認できておらず、未確認として扱う**（原稿ではこの言い回しを使わない）
- 出典：Sources ポッドキャスト（YouTube）、blog.google（Q3 決算 edited transcript）、Reuters、ceointerviews.ai（書き起こしミラー）

## 項目9：Neon for Cyber／Fairwind Program

- 主張：Neon にはサイバー防御向けの派生展開がある
- 確認できた事実：公式発表ポストに明記。「Gemini 4 Neon for cyber is rolling out to trusted defenders in the coming days as part of the Fairwind Program」。対象メンバーは今後数日で順次アクセス、申請は Cloud アカウントチーム経由。ブログにはサイバー系ベンチマーク（AutoBaxBench 等）と「Carbon 級の保護」を備える旨も記載
- 判定：**一次資料で確認**
- 食い違い：特になし
- 出典：Google 公式ブログ（Neon 発表ポスト）

## ラウンド1のまとめ

### 確認できた芯の数字

- **7週間で4モデル**：Argon 9/30 → Carbon 10/28（一般提供 11/10）→ Hydrogen 11/12 → Neon 11/18。発表日ベースで49日＝ちょうど7週間
- **価格**：Neon $3／$0.15／$15。Carbon・Argon は導入価格 $2／$10 が 11/30 まで、**12/1 から標準価格 $4／$20**（第2のニュースフック。本命公開日 12/6 はその直後）
- **ベンチマーク**：Intelligence Index は Neon 61・3位（Carbon 60）。Coding Agent Index は公式 58.6／第三者 59。タスク単価は Neon $6.86 vs Fable 5.2 $15.47
- **Argon 退場**：Gemini アプリからは退場し移行先は Neon。API では存続し、公式の廃止告知は無い
- **旧リズム**：1.0（2023-12-06）〜3（2025-11-18）の年単位の世代交代。Neon 発表日は Gemini 3 発表からちょうど1年

### 主な食い違い

1. Carbon の「発表日」：10/28（発表）と 11/10（一般提供）の混同が二次情報にある
2. 「コスト約60%」：正しくは「コストは Carbon の60%（＝40%安い）」で、起源はパートナー企業 Glean の証言。「60%安い」は誤読として不採用
3. Coding Agent Index：58.6（Google 公式）と 59（Artificial Analysis の四捨五入表記）の表記ゆれ
4. Neon の価格に期限があるとする二次情報：Carbon／Argon の導入価格終了との混同とみられ、公式に記載なし。不採用
5. Carbon の Intelligence Index：59（発表時点・v5.0）と 60（後の版／設定）の版差。原稿では版と設定を明記する

### ラウンド2で潰す残件

1. Neon モデルカード原文の直接照合（「adapted from Gemini 4 Carbon」、知識カットオフ 2026年3月）
2. 開発者ドキュメント原文の直接確認（Argon→Neon の移行案内）
3. Vertex AI／Gemini Enterprise Agent Platform での提供の公式確認
4. Pichai の「very short shelf life」発言の原文照合
5. 「最重要課題の一つ」という言い回しの有無の確認
6. Argon の API 廃止日程の有無（現時点では告知なし）
7. Google 公式価格表の原文での 12/1 改定の直接確認（対象モデルとキャッシュ価格の扱い）
8. 公開直前の鮮度チェック：12/1 価格改定の実施状況、その後のモデル発表の有無
