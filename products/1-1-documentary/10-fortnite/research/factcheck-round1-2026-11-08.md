# 1-1-10 フォートナイト（P39）裏取りラウンド1（2026-11-08）

- 対象：統合メモ（synthesis-2026-11-08.md）第3章 3-8「裏取り優先リスト」8件
- 実施：2026-11-08。公開情報の一次資料（公式発表・公式ブログ・裁判資料・公式リリース）を直接開いて照合した
- 判定の定義：「確認できた」＝一次資料の原文で該当箇所を確認。「部分的にできた」＝一次資料の特定や複数報道の一致はあるが、原文の直接読み取り等に残件がある。「未確認」＝本ラウンドで確認に至らなかった
- 本文での扱いは、統合メモ第3章の決定（特に 3-5 の3層分離、3-6 の Genie の範囲）に従う

---

## 1. Genie 4 の DeepMind 公式原文

**判定：確認できた**

- 出典：Google DeepMind 公式ブログ「Genie 4: A new generation of world simulation」（2026-10-27、Raia Hadsell／Diego Rivas／Hang Qi）
  - https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/
- 原文で確認した内容：
  - Genie 4 は「natively multimodal」で、世界と同時に音（音楽・環境音・対話）を生成する。リアルタイム世界モデルとして初めて音声をネイティブ生成する、と明記
  - Gemini ファミリーを組み込んでいる。Gemini Omni が見た目と振る舞いを現実に接地させ、Gemini 3.8 Flash がガイドエージェントとして場面を観察し、目標をステップに分解して進捗を検証する。一貫性・連続性の維持に Gemini モデルを使う
  - 自然言語でシミュレーションを実行中に変更できる（天気の変更、カメラ移動、新しい人物・物の導入）。いわゆる「実行中の世界へのテキスト介入」は公式に確認できた
  - 提供範囲：まず trusted tester 向けの研究プレビューとして展開開始。続いて Google AI Ultra 加入者（Project Genie）と、Gemini API／Google AI Studio の早期アクセスパートナーへ。Project Genie 向けには waitlist がある
  - 制約も公式に併記されている：短いセッション内でのみ一貫性を保つ、時間経過や複雑な編集の後に視覚的詳細や物体の永続性がずれる、複雑な物理相互作用・音声の正確さ・読める文字・空間的正確さ・長期の一貫性は研究途上
  - **解像度・fps・セッション長などの数値仕様は公式発表に記載がない**（二次情報にあった「最大30fps」等は公式原文にはない。本文で数値仕様には触れないこと）
- 本文での扱い：統合メモ 3-6 の前提（公式照合が済むまで Genie 4 を本文に入れない）は本ラウンドで解消した。ただし扱いの範囲は決定どおり Genie 3 と Project Genie を軸とし、Genie 4 に触れる場合も上記の公式原文の範囲内に限る

## 2. Galactus（2020-12）の同時接続1,530万人

**判定：確認できた**

- 出典：Disney 公式プレスリリース（2024-02-07、Business Wire 配信）「Disney and Epic Games to Create Expansive and Open Games and Entertainment Universe Connected to Fortnite」
  - https://www.businesswire.com/news/home/20240207879854/en/
- 該当箇所（原文）：「the Marvel Nexus War with Galactus, which drew more than 15.3 million concurrent players」（Disney と Epic の関係を深めてきた実績として、Galactus イベントが同時接続1,530万人超を集めたと明記）
- 補足：これは当事者である Disney の公式発表における記載であり、一次資料として扱える。Epic 自身の2020年当時の発表文そのものは本ラウンドでは開いていないが、数字の出所は公式発表で確定した
- 本文での扱い：同時接続1,530万人（超）を公式数字として使用可。Travis Scott の1,230万人（Epic 公式発表、sources.md で一次確認可）と並べて、有料部の「ピークは場所の価値か、イベントの価値か」の検証材料に使える

## 3. Disney の15億ドル出資の公式発表原文

**判定：確認できた**

- 出典：同上、Disney 公式プレスリリース（2024-02-07、Business Wire）
  - https://www.businesswire.com/news/home/20240207879854/en/
- 原文で確認した骨子：
  - Disney は Epic Games の株式取得のために15億ドルを出資する（"invest $1.5 billion to acquire an equity stake in Epic Games"）。複数年プロジェクトと併せた出資であり、常設ユニバースの「開発予算」として提示されたものではない。取引は規制承認等の通常の完了条件付き
  - 協業内容：Fortnite と相互運用する「まったく新しいゲームとエンターテインメントの宇宙」。新しい persistent universe では Disney／Pixar／Marvel／Star Wars／Avatar のコンテンツで「play, watch, shop, engage」でき、ファン自身が物語や体験を作って共有できる。エンジンは Unreal Engine
  - Iger CEO：「Disney にとって過去最大のゲーム分野への参入（Disney's biggest entry ever into the world of games）」
  - Sweeney：「永続的で開かれた相互運用可能なエコシステム（a persistent, open and interoperable ecosystem）」
  - 見出しには「Fortnite の1億人を超えるアクティブプレイヤーとクリエイター（more than 100 million active players and creators）」という当時の表現もある
- 本文での扱い：引用はこの原文に基づく。統合メモ 3-5 の第1層（公式発表）として使用可

## 4. Creator Economy 2.0 の原文・定義／「プレイ時間40%超」等の原典／推移データ

**判定：確認できた（定義と原典）／部分的にできた（推移データ）**

### 4-a. Creator Economy 2.0 の原文と定義

- 出典：Unreal Engine 公式ブログ「Unreal Editor for Fortnite is now available in Beta!」（2023-03-22）
  - https://www.unrealengine.com/blog/unreal-editor-for-fortnite-is-now-available-in-beta
- 該当箇所（原文）：「Engagement payouts proportionally distribute 40% of the net revenue from Fortnite's Item Shop and most real-money Fortnite purchases to the creators of eligible islands and experiences, both islands from independent creators and Epic's own such as Battle Royale.」
- 定義の確定：対象はアイテムショップと大半のリアルマネー購入の**純収益**。40%をプールし、対象アイランド（独立クリエイターの島と Epic 自身の島の双方を含む）へエンゲージメントに応じて比例配分する。留保（ペイアウトの算定）は 2023-03-01 分から

### 4-b. 「プレイ時間の40%超がクリエイター島」「アイランド総数100万超」の原典

- 原典は同じ UEFN 公式ブログ（2023-03-22）だった。該当箇所（原文）：「more than one million player-built islands have been published by their creators, and more than 40% of player game time in Fortnite is spent in creator-built content」
- あわせて同ブログには「Fortnite player accounts currently over 500 million」という当時の表明もあり、sources.md で「報道で一致」だった「5億超アカウント」も一次確認可に格上げできる

### 4-c. 公式島 vs クリエイター島の推移データの入手可否

- Epic は月次などの連続した時系列を公表していない（利用者数・プレイ時間の継続公表がないことは sources.md の全体注意どおり）
- ただし、公式の定期開示として「Fortnite Ecosystem Year in Review」があり、2024年版（公式、2025-01-22）で次の数字が原文確認できた
  - 出典：https://www.fortnite.com/news/fortnite-ecosystem-2024-year-in-review-celebrating-creators-and-looking-ahead
  - 2024年にクリエイター製ゲームで遊ばれた時間は52.3億時間で、フォートナイト全体のプレイ時間の **36.5%**
  - 2024年のクリエイターへの支払総額は **3億5,200万ドル**（2023年3〜12月との比較で +11%）
  - クリエイター数は 2023年 約24,000 → 2024年 70,000。2024年に公開されたアイランドは198,000（うち UEFN 製137,000）。1日平均で約60,000のクリエイター島が遊ばれた。全プレイヤーの70%超が Epic 製とクリエイター製の双方を遊んでいる
- 制約：2023年3月時点の「40%超」は「player game time」の割合、2024年版の「36.5%」は総プレイ時間に占めるクリエイター製ゲームの時間割合で、定義が完全には同一でない。また「Epic 公式島だけ」の割合は直接公表されておらず、非クリエイター側（約63.5%）にはバトルロイヤル以外の Epic 製モードも含まれる
- 本文での扱い：Qwen の検証ロジック（公式島 vs クリエイター島の推移でぶつける）は、公式の定期開示の範囲で「粗い推移」としてなら実施できる。使う場合は各数字の時点と定義を必ず併記し、「公式島の割合」と言い換えないこと。連続時系列が取れない点は、統合メモ 3-2 の留意どおり「永続性は一部しか確認できない」判定の根拠として明示できる

## 5. Disneyland Game Rush／Smugglers Gambit の Disney Parks 公式原典

**判定：確認できた（両方とも）**

- Disneyland Game Rush：Disney Parks Blog 公式記事「Celebrate 70 Years of Disneyland in Fortnite」（Disneyland 70周年、Disney 初の Fortnite アイランド、アイランドコード 4617-4819-8826、ミニゲーム群）
  - https://disneyparksblog.com/disney-experiences/celebrate-70-years-of-disneyland-with-new-fortnite-experience/
- Smugglers Gambit：Disney Parks Blog 公式記事「Smuggler's Gambit Connects Disney Parks and Fortnite」（2026-08-15 公開、D23 で発表）
  - https://disneyparksblog.com/disney-experiences/smugglers-gambit-fortnite-disney/
  - 骨子：Millennium Falcon: Smugglers Run | Fortnite として 2026-08-16 に開始。アトラクションと連動する初の試み。Smugglers Gambit は Disney Games and Digital Entertainment が内製した Fortnite アイランド（惑星 Ord Ryla の Mersa Veta Station）。アプリ（Disneyland アプリ／My Disney Experience）でミッションを受け、MyDisney アカウントと Epic アカウントの連携で報酬（Forsworn Trooper Outfit 等）を受け取る
- 本文での扱い：統合メモ 3-5 の第2層（公式に確認できる実現）として、TechRadar 等の報道経由でなく Disney Parks Blog を出所に書ける

## 6. Bloomberg（2026-10-12）報道と Sweeney の同日発言の原文

**判定：部分的にできた**

- Bloomberg 原文（Jason Schreier、2026-10-12「Epic Games delays Disney project, asks developers to use more AI」）は有料壁の内側で、本ラウンドでは全文を直接読めていない。ただし、その内容は複数の媒体（GamesIndustry.biz／VGC／Eurogamer／PC Gamer／Engadget／Kotaku／Ars Technica 等）が一貫して伝えており、次の骨子は報道として確定できる：
  - 未発表の Disney シューター（Marvel／Star Wars のキャラクターが登場）は 2027年3月の目標が後退し、新しい日程はチームに示されていない
  - 開発チームに「AIファースト」への移行が伝えられた（Anthropic の Claude 等のツールを使い、人間が監督する）。あるゲームディレクターの内部メッセージとして「No more hand-written code」、アートは「generated with full AI workflows」
  - 背景として、プロジェクトは想定より人員と時間を要し遅れていた、とされる
  - なお 2026年4月の Bloomberg 報道では、Disney 協業のプロジェクトは3件あり、同シューターは当初 2026年11月目標だったとされていた（つまり目標は 2026-11 → 2027-03 → 後退、という変遷自体が報道で追える）
- 公式側の原文として確認できたもの：
  - Epic 広報（コミュニケーションディレクター Jake Jones）の Bloomberg への公式コメント：「We're embracing AI-accelerated development, led by Epic developers who are the visionaries and creative drivers for everything we do.」（複数の媒体が同一文面で引用）
  - Sweeney の X 投稿（2026-10-12、同日）：「We have a huge pivot underway here at Epic, moving developers around to retool for maximum AI acceleration. The aim isn't to do the same stuff with fewer people, but to enable everyone here to build MORE and BETTER stuff, and to bring the benefits to all teams using Unreal.」（複数の媒体が同一文面で引用。X 原文そのものの直接表示は本ラウンドでは行っていない）
  - Disney はコメントを避けたと報じられている（GamesRadar）
- 重要な線引き：**遅延と2027年3月という目標自体は、Epic も Sweeney も公式には確認していない**。公式に確認できるのは「AI 加速への再編が進行中」という表明まで
- 本文での扱い：統合メモ 3-5 の第3層として、「Bloomberg は〜と報じた」「Sweeney は同日、X で〜と述べた」の主語明示で使う。遅延を公式事実のように書かない

## 7. 裁判資料のフォートナイト収益「90億ドル超」

**判定：部分的にできた（該当資料は特定できたが、原本の直接読み取りは未了）**

- 該当資料：Epic v. Apple 訴訟の公判初日（2021-05-03）に示された Epic の財務プレゼンテーション（2020年1月時点の取締役会向け資料）。DocumentCloud で公開されている（文書番号 20696836「epic-apple-trial-epic-games-exhibit.pdf」）
  - https://assets.documentcloud.org/documents/20696836/epic-apple-trial-epic-games-exhibit.pdf
- 資料の内容として複数媒体（The Verge／GamesIndustry.biz／TechSpot 等）が当該資料から報じた数字：フォートナイトの収益は 2018年 約54億ドル、2019年 約37億ドル、2年合計で90億ドル超（集計の版により 91億ドル／91.7億ドルと表記が揺れる。別の Epic 財務資料では総収益ベースで 2018年 56.28億ドル＋2019年 42.21億ドル＝96.49億ドルという数字も報じられている）
- 本ラウンドの残件：DocumentCloud の PDF 原本はアクセス制限（403）で直接開けず、該当ページの文面そのものは読み取れていない
- 本文での扱い：統合メモのルール（確認できるまで使わない、Claude の指摘）を踏まえ、**「90億ドル」を単独の確定数字としては使わない**。使う場合は「Epic v. Apple 訴訟で公開された Epic の財務プレゼンテーションによれば、フォートナイトの収益は2018年と2019年の合計で90億ドルを超えていた」と出所を明示する形に限り、原稿化の最終段階で原本（DocumentCloud または裁判所のエキシビット）の該当箇所を再確認すること

## 8. 登録「4億超」の判決文・FTC 原文／MAU 7,830万の一次出所

**判定：確認できた（両方とも）**

### 8-a. 登録「4億超」

- 判決文：Epic Games, Inc. v. Apple Inc.、Rule 52 Order After Trial on the Merits（Case 4:20-cv-05640-YGR、Dkt. 812、2021-09-10）の事実認定に「Fortnite is Epic Games' most popular game and app, with over 400 hundred million registered players worldwide.」と明記されている（脚注29付き。Justia 掲載の判決 PDF で該当箇所を確認）
  - https://cases.justia.com/federal/district-courts/california/candce/4:2020cv05640/364265/812/0.pdf
- FTC 原文：FTC プレスリリース「Fortnite Video Game Maker Epic Games to Pay More Than Half a Billion Dollars over FTC Allegations of Privacy Violations and Unwanted Charges」（2022-12-19）でも、フォートナイトには世界で4億人を超えるプレイヤー／ユーザーがいる旨が述べられている（「more than 400 million」）
  - https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations
- 注意：判決の事実認定が依拠するデータは公判時点（〜2021年）のもので、「登録プレイヤー」は累計アカウント数であり現在のアクティブ数ではない。本文では時点と定義を併記すること

### 8-b. MAU 7,830万（2018-08）の一次出所

- 一次出所は Epic 公式ブログ（2018-09-20、Fall Skirmish 発表）の次の一文だった：「August was Fortnite's biggest month yet, with 78.3 million of you showing up to play.」
- Polygon／GameSpot／Nintendo Life 等の当時報道が、いずれも epicgames.com の当該ブログを出所として同一文面を引用している
- 本文での扱い：「2018年8月には月間7,830万人がプレイした（Epic 発表）」として使用可。ただし Epic 自身はこれを「MAU」とは呼んでおらず、「その月に遊んだ人数」という表現である点に注意する

---

## まとめ：原稿化への進み方

- 一次確認が済んだもの（そのまま原稿の材料にできる）：項目1（Genie 4、ただし範囲は決定どおり限定）、2（Galactus）、3（Disney 発表）、4-a／4-b（Creator Economy 2.0 と40%・100万の原典）、5（Game Rush／Smugglers Gambit）、8（4億超／7,830万）
- 制約付きで使えるもの：項目4-c（推移は公式の定期開示による粗い推移のみ。定義の違いを併記）、項目6（Bloomberg は主語明示の報道として。遅延は公式未確認）、項目7（90億ドルは出所明示の条件付き。原本の再確認が原稿化最終段階の宿題）
- 未確認のまま残るもの：なし（8件すべてに判定が付いた）。ただし項目6の Bloomberg 原文全文と項目7のエキシビット原本は、原稿化直前の再確認リストに残す
- 判定への影響：有料部の決め手の検証（ピーク＝Galactus 1,530万 vs クリエイター島の推移）は、一次資料の範囲で実施可能になった。推移データの粗さそのものが「永続性は一部しか確認できない」という条件付き判定を支える材料になる
