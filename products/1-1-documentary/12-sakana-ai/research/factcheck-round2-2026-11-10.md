# 裏取りレポート ラウンド2：サカナAI（1-1-12）

- 実施日：2026-11-10
- 対象：企画ブリーフ（訂正済み）／裏取りラウンド1／統合メモの決定事項（2026-11-10 オーナー承認済み）
- 目的：ChatGPT の要求3点＋Claude の宿題2件＋追加確認2件を一次情報で判定し、原稿化に使える一次資料を棚卸しする
- 判定の定義：＝一次情報（原論文・公式サイト・公式プレスリリース）で確認／＝信頼できる報道のみで確認／＝裏が取れなかった

---

## 1. Evolutionary Model Merge の独立評価（ChatGPT 要求1）

### 問いの形
サカナAI自身の発表・論文以外に、第三者による評価・検証があるか。ベンチマーク主張を第三者はどう評価しているか。

### 検証結果

**（a）学術査読という形の外部検証は存在する**
- 原論文は Nature Machine Intelligence に掲載（2025年1月27日オンライン公開、Vol.7, pp.195–204、DOI: 10.1038/s42256-024-00975-8）。arXiv 版（2024年3月）から査読を経て、追加実験を含む改訂版として掲載された
- 査読後に補強された補足資料には、手法への当然の疑義に応える実験が並ぶ：未最適化マージ（TIES／DARE-TIES／Frankenmerging）との比較、同一データでのファインチューニング対照、無関係モデルを最大8個混ぜる「distraction」実験（性能は劣化するが崩壊しない）、13B モデルへのスケーリング確認。つまり「身内の自己申告」ではなく、査読プロセスを通った主張ではある

**（b）第三者による実装・採用は存在する**
- Arcee AI のオープンソース基盤 mergekit に `mergekit-evolve` が実装されている。公式ドキュメントは「SakanaAI's Evolutionary Optimization of Model Merging Recipes に inspired by」と明記し、CMA-ES でマージ係数をベンチマーク指標に対して最適化するサカナ方式（パラメータ空間）を第三者が再実装したもの
- サカナAI公式ブログ（2025年1月28日更新分）は、手法が mergekit と Optuna Hub に実装され、外部ユーザーが多数の派生モデルを公開していると述べている（会社側の記述だが、mergekit 側のドキュメントで裏が取れる）
- 後続の学術研究でも採用・引用が進んでいる。例：ICML 2026 の論文「Bridging Spherical Black-Box Optimizers」は、進化的モデルマージを Mistral-7B 系＋MGSM というサカナと同系統のセットアップで検証対象として取り上げ、「マージは多峰性（multi-modal）である」等の分析を行っている。他にも LS-Merge、PopuLoRA 等が「EvolMerge（Akiba et al., 2025）」として引用・発展させている

**（c）第三者によるベンチマーク実測は「別物差し」で部分的に存在する**
- 楽天のモデルカード（RakutenAI-2.0-mini-instruct）には、楽天自身の評価プロトコルで測った Japanese MT-Bench の実測値として EvoLLM-JP-v1-7B＝4.58、EvoLLM-JP-A-v1-7B＝3.80 が掲載されている。第三者が独立に測った数値が存在すること自体は確認できる
- ただし、EvoLLM-JP の看板数値そのもの（MGSM-JA 52.0、JP-LMEH 平均 70.5＝いずれも論文・会社発表値）について、第三者機関が同じ物差しで再測定した結果は、本ラウンドでは確認できなかった

**（d）批判・留保の所在**
- 構造的な論点：この手法の適合度（fitness）はベンチマーク得点そのものであるため、「最適化対象のベンチマークへの過適合」は手法論として常につきまとう。進化計算×LLM のサーベイ論文等も、ベンチマーク過適合・チェリーピッキングへの警戒を一般論として挙げている
- 論文側の対策は明記されている：fitness 評価には MGSM のテストセットと重ならない GSM8K テスト残り 1,069 サンプルを日本語化して使い、テストセットは最適化から厳密に分離した、と Methods に明記。JP-LMEH は最適化対象外のベンチマーク群で汎化を主張する構成
- 技術メディアには、別件（2025年2月の「AI CUDA Engineer」の性能主張がベンチマークの欠陥によるものと判明し同社が訂正した件）を引き、「同社の大きな主張には査読に耐えなかった前歴がある」と慎重な見方を示す報道もある（Hackster）。ただしこれはマージ手法とは別プロジェクトの話であり、マージ手法そのものへの反証・再現失敗の報告は本ラウンドでは見つからなかった

### 判定
（査読掲載・第三者実装・後続研究での採用は一次情報で確認。看板ベンチマーク数値の第三者による同一物差し再測定は未確認）

### 原稿での扱い
- 「第三者評価が皆無」でも「独立に実証済み」でもなく、「査読と実装と引用という形の学術的受容は進んだが、看板数値の独立再測定はまだない」と段階を分けて書く
- CUDA Engineer 件は、会社の主張文化への留保として触れるなら、マージ手法とは別件であることを明記する

### 出典URL
- https://www.nature.com/articles/s42256-024-00975-8
- https://github.com/arcee-ai/mergekit/blob/main/docs/evolve.md
- https://sakana.ai/evolutionary-model-merge/
- https://huggingface.co/Rakuten/RakutenAI-2.0-mini-instruct
- https://www.hackster.io/news/sakana-ai-promises-better-ai-by-teaching-large-language-models-the-art-of-cooperation-a9d451ff919e

---

## 2. 同一条件でのコスト比較（ChatGPT 要求2）

### 問いの形
進化的モデルマージのコスト（計算量・GPU時間）と、同等性能モデルを通常の学習で得るコストを、同じ物差しで比較できる資料があるか。

### 検証結果

**結論を先に：GPU時間の物差しでの同一条件比較は、一次資料には存在しない。**

**（a）「同じ物差し」の比較として実在するのは、性能面の対照実験（論文補足資料）**
- Nature Machine Intelligence 論文の補足資料 §2.1.2「Comparison with Fine-tuning」は、進化マージの fitness に使ったのと同一データ（日本語化 GSM8K 1,069 サンプル）で、3つのソースモデルそれぞれに LoRA／フルパラメータのファインチューニングを行い、同じ物差し（MGSM-JA／JP-LMEH）で比べている
- 結果（補足表1）：進化マージ（PS）は MGSM-JA 52.0／JP-LMEH 70.5。ファインチューニングの最良は LoRA・WizardMath の MGSM-JA 43.2 どまりで、しかも FT は JP-LMEH を大きく悪化させる例が目立つ（壊滅的忘却）。つまり「同一データ・同一評価での性能比較」は存在し、マージ側が勝ったという形で査読を通っている
- ただしこの対照は「同等性能を通常学習で得る場合」ではなく「同じ少量データで FT した場合」との比較である点に注意

**（b）マージ側のコストとして公表されているのは「探索の規模」だけ**
- パラメータ空間（PS）の最適化：CMA-ES（Optuna 実装）で 1,000 試行。各試行は 1,069 サンプルの精度評価。データフロー空間（DFS）：128 個体×100 世代
- 論文・ブログとも、マージ実行そのものの総 GPU 時間・総コストの金額換算は公表していない。主張は定性的（"without requiring extensive additional training data or compute"、勾配学習なし）にとどまる

**（c）傍証として使える数字**
- 論文補足資料は、ソースモデルの土台の一つ japanese-stablelm-base-gamma-7b の日本語ファインチューニングが 100B トークン規模で「10,000 GPU 時間超」の計算コストだったと指摘し、「ソースモデル群の全学習データを揃えて再学習する比較は不可能」と自ら明記している。これは裏返すと、マージは「10,000 GPU 時間級の投資を含む系譜の上に、勾配計算ゼロで乗っている」手法だという構造を示す数字でもある
- 第三者の実務者ガイド（GPU クラウド事業者 Spheron の 2026 年記事）による進化マージの実測見積では、13B モデル・100 回評価の進化スイープで約 12 GPU 時間（H100 レンタル換算で約 24 ドル）とされている。ベンダーブログの概算であり一次資料ではないが、桁感（＝事前学習や大規模 FT とは桁が違う）の参考にはなる

### 判定
（同一条件の「性能」比較は論文補足に実在。「GPU 時間・金額」での同一条件コスト比較は存在しない——この不在自体を明記すべき事項）

### 原稿での扱い
- 有料部の問い（コストと性能の関係）に対しては、「安いのは確かだが、物差しの揃ったコスト比較は誰も出していない。比較可能なのは性能対照実験と探索規模の公表値だけ」と書くのが正確
- 使える数字：PS 最適化 1,000 試行／fitness 評価 1,069 サンプル／親モデルの系譜に 10,000 GPU 時間超の FT が含まれる（論文補足）。「マージはタダ同然」という単純化も「通常学習と同等」という単純化も、一次資料からは言えない

### 出典URL
- https://static-content.springer.com/esm/art%3A10.1038%2Fs42256-024-00975-8/MediaObjects/42256_2024_975_MOESM1_ESM.pdf
- https://d-nb.info/136512195X/34 （論文本文 PDF）
- https://www.spheron.network/blog/model-merging-gpu-cloud-ties-dare-slerp-evolutionary/

---

## 3. 事業化の証拠（ChatGPT 要求3）

### 問いの形
MUFG・大和証券の進展、その他の導入事例・売上に関する公表情報を、公式発表ベースで確認する。

### 検証結果

**MUFG（三菱UFJ銀行）——「実案件での検証」段階まで進展（公式発表あり）**
- 2026年3月6日、サカナAIが公式発表：「AI融資エキスパート」が約半年間の概念実証（PoC）を経て実案件での検証フェーズへ。約100名が参加（うち約30名がコア）、一部拠点での検証で「特定案件における実業務適用の到達を確認」、今後は全国の営業店への段階的展開を目指す、という内容
- ただし段階の切り分けは必要：MUFG の 2026年5月19日の決算説明会資料では「AI融資エキスパート」は「開発中」の扱いで、全行本番稼働を示す公式発表はない。到達点は「実案件検証」であって「本番運用開始」ではない

**SMBCグループ——「実務への適用開始」まで到達（双方の公式リリースあり）**
- 2026年4月30日、SMBCグループとサカナAIが発表：2025年5月のパートナーシップ契約の「実装フェーズ第一号案件」として「提案書自動生成アプリケーション」を開発し、三井住友銀行において実務への適用（導入）を開始。現時点で最も「本番」に近い公式事例

**大和証券グループ——「本番開発フェーズ」移行（3社連名・適時開示）**
- 2026年8月5日、大和証券グループ本社・大和証券・サカナAIの3社連名で発表（上場企業の適時開示として出された）。2025年10月のパートナーシップに基づく総資産コンサルティングプラットフォームが、技術検証フェーズを経て 2026年8月1日付で本番開発フェーズへ移行。なお言葉の正確さとして、これは「本番開発」であって「本番稼働」ではない

**防衛分野——受注の公式発表あり（金額は公表資料ベース）**
- 2026年8月24日、サカナAIが公式発表：防衛省「総合分析業務に必要なAI機能の調査・実証」を受注（契約締結は 2026年7月29日、対象は情報本部の総合分析業務）。防衛装備庁が公表した契約情報では契約額 3億2,903万2,000円とされる（公表資料に基づく報道・二次資料で確認。金額は会社の発表文には含まれていない）
- 2026年3月には防衛装備庁の防衛イノベーション科学技術研究所（DIST）との委託研究契約（自衛隊の指揮統制システム高度化）も発表済み

**その他の提携**
- 住友商事・SCSK との業務提携は 2026年11月に報道されたが（ラウンド1で公式発表が確認できなかった件）、本ラウンドでも双方の公式プレスリリースは直接確認できず、報道ベースの扱いを維持する

**製品化（課金プロダクトの販売開始）**
- 2026年6月15日に商用製品「Sakana Marlin」、同年6月22日に「Sakana Fugu」が一般提供開始。公式サイトに Fugu の製品ページと API 価格（Fugu Ultra：入力 $5／出力 $30・100万トークン等）が掲載され、課金プロダクトとして販売されていることは公式サイト側で確認できる。公式サイトのトップページも MUFG Bank／SMBC Group／Daiwa Securities Group／防衛省／防衛装備庁／総務省を協働先として明示している

**売上に関する公表情報**
- 売上高そのものの公式開示はない（非上場で開示義務もない）。日経報道の「2027年の年換算売上高 300億円超（2026年見通しの10倍超）」は見込み値の報道ベースであり、ラウンド1の扱い（本文の主張に使わない）を維持する。金額が公表資料で裏付けられる収益の実例は、防衛装備庁契約（約3.3億円）など個別契約レベルにとどまる

### 判定
（MUFG・SMBC・大和証券・防衛省について、段階の異なる公式発表で事業化の進展を確認。売上高の公式開示はなし）

### 原稿での扱い
- 統合メモの4段階区分（研究発表／技術実証／本番運用／収益化）で書くと正確になる：MUFG＝実案件検証、SMBC＝実務適用開始、大和証券＝本番開発、Fugu／Marlin＝課金製品として販売開始。ただし「収益化の規模」は未開示と明記
- 事業性の判定材料としては「大企業の公式発表が段階を追って前進している」ことは強い証拠だが、「いくら稼いでいるか」は依然として闇の中、という非対称がこの会社の事業性の実像

### 出典URL
- https://sakana.ai/mufg-ai-lending/ （MUFG・2026年3月6日発表）
- https://sakana.ai/mufg/ （MUFG・2025年5月パートナーシップ）
- https://www.smbc.co.jp/news/pdf/j20260430_01.pdf （SMBCグループ・2026年4月30日発表）
- https://sakana.ai/smbc-proposal-ai/
- https://www.daiwair.co.jp/td_download.cgi?c=8601&i=3269328 （大和証券グループ・2026年8月5日適時開示）
- https://sakana.ai/daiwa-shoken-full-scale/
- https://sakana.ai/defense-integrated-analysis/ （防衛省受注・2026年8月24日発表）
- https://sakana.ai/fugu/ （製品ページ・価格）
- https://sakana.ai/ （協働先の明示）

---

## 4. The AI Scientist の Nature 掲載（Claude 宿題1）

### 問いの形
ラウンド1レポート内に出典なしで書かれた「AI Scientist の Nature 掲載」は実際に一次確認できるか。

### 検証結果
- **実在する**。Lu, C. et al.「Towards end-to-end automation of AI research」が Nature に掲載された（DOI: 10.1038/s41586-026-10265-5、Nature 651、2026年3月25〜26日公開）。サカナAIも 2026年3月26日に「The AI Scientist: Towards Fully Automated AI Research, Now Published in Nature」と公式発表している
- ただしラウンド1の記述（「その後、発展版の成果が Nature 誌に掲載された」）は切り分けが不正確で、以下の2つを混ぜている：
1. Nature 論文は、**人間の研究者たちが AI Scientist というシステム自体を記述した論文**である。「AI が書いた論文が Nature に載った」のではない
2. AI 生成論文の査読通過は別件で、ICLR 2025 のワークショップ（ICBINB）に提出した3本のうち1本が平均 6.33（6／7／6）で通過したもの。事前合意に基づき採択後に撤回されており、出版はされていない
- この2つを融合した「AI が Nature 論文を書いた」という言説が流通しており、第三者のファクトチェック記事がこの混同を明示的に指摘している。原稿で触れる場合は、この切り分け自体が検証記事の見せ場になる

### 判定
（Nature 掲載は一次情報で確認。ただしラウンド1の記述は要修正：Nature 論文＝システムを記述した人間著者の論文、AI 生成論文の査読通過＝ICLR ワークショップの別件）

### 原稿での扱い
- 書くなら「AI Scientist の研究をまとめた論文が Nature に掲載された（2026年3月）。なお、AI 自身が生成した論文の査読通過は ICLR 2025 ワークショップでの1本で、合意のうえ撤回され未出版」と2文に分ける

### 出典URL
- https://www.nature.com/articles/s41586-026-10265-5
- https://sakana.ai/ai-scientist-nature/
- https://sakana.ai/ai-scientist-first-publication/ （ICLR ワークショップ査読通過の公式発表）

---

## 5. 英語圏での会社の発信（Claude 宿題2）

### 問いの形
公式サイト・公式ブログ・論文など、英語での一次発信の実態（"collective intelligence" 等の原文表現を含む）。

### 検証結果
- 公式サイト sakana.ai は英語・日本語の両方で運用され、主要な研究発表は英語ブログが一次発信になっている（資金調達や提携の一部は日本語先行／並行）。論文は arXiv の英語論文が基本形
- "collective intelligence" の原文表現は複数箇所で確認できる：
- Evolutionary Model Merge の英語発表（2024年3月21日）："The core research focus of Sakana AI is in applying nature-inspired ideas, such as evolution and collective intelligence, to create new foundation models"、および "By working with the vast collective intelligence of existing open models"
- 論文（Nature Machine Intelligence）要旨でも "harnessing their collective intelligence" と表現
- M2N2 の英語発表（2025年8月25日）："Like a school of fish, where collective intelligence emerges from the group"、"This nature-inspired approach is central to Sakana AI's mission to find new foundations for AI based on collective intelligence"
- 現在の公式サイト（英語トップ）のタグラインは "Building Frontier AI in Japan" で、"Our work on evolution, collective intelligence, and self-improving systems appears at ICLR, NeurIPS, and in Nature, and ships in our products" と自己定義している
- 英語圏メディアへの発信も継続している：シリーズBは TechCrunch が CEO 発言込みで報じ、IPO 報道についても英語圏で「近い将来の IPO 計画はない」旨の会社コメントが伝えられている

### 判定
（英語での一次発信は公式ブログ・論文・公式サイトで恒常的に行われており、"collective intelligence" は創業初期からの原文表現であることを確認）

### 原稿での扱い
- 「日本国内だけの会社」という像は誤りで、研究発信の主戦場は最初から英語圏（arXiv／国際会議／Nature 系誌）。事業（顧客）は日本、研究の名声は英語圏、という二層構造として書ける

### 出典URL
- https://sakana.ai/evolutionary-model-merge/
- https://sakana.ai/m2n2/
- https://sakana.ai/
- https://www.nature.com/articles/s42256-024-00975-8

---

## 6. IPO 報道のその後（追加確認）

### 問いの形
2026-11-09 の日経報道以降、会社側の公式コメントに変化があるか、続報があるか。

### 検証結果
- 本ラウンド実施時点（2026-11-10）で、11月9日の報道群以降に会社から出た新しい公式発表・コメントの変化は確認できない
- 9日当日の追随報道（共同通信・時事通信・朝日新聞・Reuters 等）はいずれも同一の会社コメント「IPOを正式に決定した事実はない。引き続き、世界最先端の技術開発と、日本でのAIの社会実装にまい進する」を併記しており、Reuters の続報でも文面は同一。英語圏でも "no near-term IPO"（近い将来の IPO はない）という趣旨で伝えられている
- つまり報道から1日時点では「関係者取材による準備報道＋会社の正式決定否定」というラウンド1の構図に変化はない

### 判定
（変化なしを確認。会社コメントは不変で、新規の公式発表はなし）

### 原稿での扱い
- ラウンド1の両建て方針（報道は報道、決定は未決定）をそのまま維持。公開は2027年前半の決定済みであり、IPO 続報は続編・追補で受ける

### 出典URL
- https://www.newsweekjapan.jp/articles/-/339525 （Reuters 続報）
- https://www.daily.co.jp/society/economics/2026/11/09/0021017678.shtml （共同通信配信）

---

## 7. 検証5軸に使える一次資料の棚卸し（追加確認）

原稿化の際に直接引ける一次資料の一覧。URL はすべて本ラウンドで実在を確認したもの。

### 性能
- Evolutionary Model Merge 原論文（Nature Machine Intelligence、DOI: 10.1038/s42256-024-00975-8）：https://www.nature.com/articles/s42256-024-00975-8
- 同 arXiv 版（arXiv:2403.13187）：https://arxiv.org/abs/2403.13187
- 同 補足資料（ベースライン比較・FT 対照・頑健性実験）：https://static-content.springer.com/esm/art%3A10.1038%2Fs42256-024-00975-8/MediaObjects/42256_2024_975_MOESM1_ESM.pdf
- 公式発表ブログ（2024年3月21日、Nature 掲載の追記あり）：https://sakana.ai/evolutionary-model-merge/
- 後継：M2N2（arXiv:2508.16204、GECCO'25）：https://sakana.ai/m2n2/ ／ CycleQD（arXiv:2410.14735、ICLR 2025）
- AI Scientist の Nature 論文（DOI: 10.1038/s41586-026-10265-5）：https://www.nature.com/articles/s41586-026-10265-5
- Darwin Gödel Machine（arXiv:2505.22954）：https://sakana.ai/dgm/

### コスト
- 論文補足資料 §2.1.2（同一データでの FT 対照実験、japanese-stablelm-base-gamma-7b の 100B トークン／10,000 GPU 時間超への言及）：上記 Springer 補足資料 PDF
- 論文 Methods（PS 最適化 1,000 試行・fitness 1,069 サンプル等の探索規模）：上記 Nature 論文／PDF https://d-nb.info/136512195X/34
- （参考・第三者概算）Spheron の実務者ガイド（進化スイープ約 12 GPU 時間の見積）：https://www.spheron.network/blog/model-merging-gpu-cloud-ties-dare-slerp-evolutionary/

### 再現性
- 公式コード（論文の Code availability で明示、評価再現用コードを含む）：https://github.com/SakanaAI/evolutionary-model-merge （Zenodo DOI: 10.5281/zenodo.14241914）
- 第三者実装 mergekit-evolve（Arcee AI）：https://github.com/arcee-ai/mergekit/blob/main/docs/evolve.md
- モデル重みは Hugging Face で公開（SakanaAI/EvoLLM-JP-v1-7B 等）。第三者実測の例：https://huggingface.co/Rakuten/RakutenAI-2.0-mini-instruct

### 適用範囲
- 論文本文・補足の前提条件：パラメータ空間のマージは「同一ベースモデルのファインチューン同士」が前提。完全に独立に学習されたモデル同士のマージは permutation invariance 等のため困難と論文自身が明記。データフロー空間は異なるモデルのレイヤー接続も可能だが、対象や規模に制約（論文では2モデルまで、単一 GPU で動く規模を想定）
- つまり適用範囲の一次資料は論文そのもので、「何でも融合できる」ではなく「同じ土台から枝分かれしたモデル群」が主戦場、と書ける

### 事業性
- MUFG パートナーシップ（2025年5月）：https://sakana.ai/mufg/ ／ AI融資エキスパート実案件検証（2026年3月）：https://sakana.ai/mufg-ai-lending/
- SMBC 実装フェーズ第一号（2026年4月）：https://www.smbc.co.jp/news/pdf/j20260430_01.pdf
- 大和証券 本番開発フェーズ移行（2026年8月・適時開示）：https://www.daiwair.co.jp/td_download.cgi?c=8601&i=3269328
- 防衛省受注（2026年8月）：https://sakana.ai/defense-integrated-analysis/
- 製品・価格（Fugu）：https://sakana.ai/fugu/
- 資金調達：シリーズA https://sakana.ai/series-a/ ／シリーズB拡大の公表はラウンド1参照（2026年4月9日更新、総額約320億円・評価額約4,320億円・累計約$412M）

---

## 総括

| # | 項目 | 判定 |
|---|---|---|
| 1 | Model Merge の独立評価 | （査読・第三者実装・後続研究での採用は確認。看板数値の同一物差しでの独立再測定は未確認） |
| 2 | 同一条件でのコスト比較 | （性能の同一条件比較は論文補足に実在。GPU時間・金額での同一条件比較は存在しない） |
| 3 | 事業化の証拠 | （MUFG＝実案件検証／SMBC＝実務適用開始／大和証券＝本番開発／防衛省＝受注、すべて公式発表で確認。売上高の公式開示はなし） |
| 4 | AI Scientist の Nature 掲載 | （実在を一次確認。ただしラウンド1の記述は要修正） |
| 5 | 英語圏での会社の発信 | （英語ブログ・論文が一次発信として恒常化。"collective intelligence" の原文表現を確認） |
| 6 | IPO 報道のその後 | （2026-11-10 時点で続報・公式コメントの変化なし） |
| 7 | 一次資料の棚卸し | （5軸すべてに原稿で使える一次資料を確保。コスト軸のみ「比較データの不在」が結論） |

### ラウンド1からの修正・進展

1. **AI Scientist の Nature 掲載の記述**：ラウンド1の「発展版の成果が Nature 誌に掲載された」は不正確。正しくは「AI Scientist システムを人間研究者が記述した論文が Nature に掲載（2026年3月、DOI: 10.1038/s41586-026-10265-5）」。AI 生成論文の査読通過は ICLR 2025 ワークショップの別件で、撤回済み・未出版
2. **MUFG の到達段階**：ラウンド1時点の「パートナーシップ契約＋文書作成自動化」から、2026年3月に「AI融資エキスパートの実案件検証フェーズ」へ前進。ただし本番稼働の公式発表はまだない
3. **事業化の公式事例がラウンド1以降に積み上がっている**：SMBC の実務適用開始（2026年4月）、大和証券の本番開発移行（2026年8月）、防衛省の受注（2026年8月、契約は7月）、商用製品 Fugu／Marlin の販売開始（2026年6月）。「研究会社から事業会社へ」の第3部の材料は、公式発表だけで時系列が組める状態になった
4. **評価額・調達額は変更なし**：シリーズB総額 約320億円・評価額 約4,320億円（2026年4月の会社公表）が引き続き最新の公式数値。本ラウンドで新しい資金調達の公式発表は確認されなかった
5. **有料部の問いへの含意**：「コストと性能の関係」については、①性能の物差しでは同一条件比較があり査読を通った、②コストの物差しでは同一条件比較が存在せず、会社も総コストを開示していない、③ただし親モデルの系譜コスト（10,000 GPU 時間超の FT 等）を「ただ乗り」している構造は一次資料から言える——この3点セットが、問いへの判定の核になる
