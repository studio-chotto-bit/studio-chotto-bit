# 1-1-10 フォートナイト（P39）ディスカッション依頼文（2026-11-08 準備）

repo 集約済み（コミット ede0a3a、products/1-1-documentary/10-fortnite/、全ファイル照合済み）。
Discussion の開設と各AIへの依頼はブラウザ作業（下記「実施メモ」参照）。

## Discussion（開設時にそのまま使う）

- リポジトリ: studio-chotto-bit/studio-chotto-bit
- タイトル: `1-1-10 フォートナイト（P39）企画ディスカッション`
- 本文: 下記「共通依頼文」と同一の文面をそのまま投稿する
- 各AIの返答は、サービス名を見出しにしたコメントとしてこの Discussion に投稿し、投稿後に読み戻して確認する

## 共通依頼文（Discussion 本文＝各AIへこのまま送る文面）

新しい有料記事（note、¥500）の企画について、率直な意見をください。素材は次の2ファイルです。

- 企画書: https://github.com/studio-chotto-bit/studio-chotto-bit/blob/main/products/1-1-documentary/10-fortnite/brief-2026-11-08.md
- 一次資料・裏取りリスト: https://github.com/studio-chotto-bit/studio-chotto-bit/blob/main/products/1-1-documentary/10-fortnite/research/sources.md

企画の骨子は次のとおりです。フォートナイトを題材に、「世界（中に入れる場所）を誰が作るのか」の移行——開発者が作る場所から、プレイヤーとクリエイターが作る場所（UEFN）へ——を描きます。価値の源泉は「人が集まり続ける永続性とIP」にあった、という仮説を検証する構成で、山場はディズニーの15億ドル出資と常設ユニバース計画、最後に「AI が世界を生成する」Genie の登場を置きます。無料3部＋有料1部の連載で、有料部で命題の判定を行います。

論点は次の7つです。

1. 中心命題「フォートナイトが作ったのは、ゲームそのものではなく『人が集まり続ける場所』だった」は検証に耐える主張か。最強の反論は何か。
2. 4部の配分（第1部＝「集まる場所」への変質／第2部＝作り手の交代／第3部＝ディズニーの15億ドルと「常設」の難しさ／有料部＝検証台帳と Genie への橋）は妥当か。有料部に残すべき「答え」は何か。
3. 仮タイトル『フォートナイトは、何を作っていたのか』の評価と代替案。無料部のタイトルが答えを漏らしていないか。
4. ディズニー常設ユニバースは公式未発表の部分が大きく、遅延や「AIファースト」転換は報道ベース（Bloomberg）である。これを第3部の山場に据えることの是非と、報道の扱いの線引き。
5. 有料部の最後に置く Genie（世界モデル）の扱い。次の製品（1-1-11）で Genie 本体を扱う前提で、どこまで書くのが適切か。
6. Roblox／Minecraft との比較は必要か。入れるとしたら分量と置き場所は。
7. リスク：出典の弱い数字の扱い、IP への配慮、フォートナイト未経験の読者への入口、未発売プロジェクトの記述リスク。

各論点に短く答え、最後に「この企画で一番直すべき点」を1つ挙げてください。

## サービス別の経路（実績のある手順）

- **Qwen**: GitHub URLを直接読める。依頼文のまま送る。
- **Grok**: サインインは Google 経由（「Googleで続ける」）。X経由は使わない。
- **ChatGPT**: プロジェクト内のチャットで開始し、依頼文に論点をすべて含める（Discussion自体は読めない前提）。repoファイルは自前のGitHub連携で読める。
- **Gemini**: URL読み取りが不安定。読めなければ企画書と資料集のファイルを添付して送る（添付元はローカル ~/workspace/goals/paid-note-article-preparation/p39/brief-2026-11-08.md と sources.md）。
- **Claude**: 最低モデル（Haiku）、統合依頼はこの1回のみ。追加のやり取りをしない。枠（5時間上限）に当たったら同窓では再試行せず、リセット時刻を記録して報告する。

## 実施メモ（ブラウザ作業者向け）

1. GitHub の repo 画面から Discussion を新規作成し、タイトルと本文（共通依頼文）を投稿する。作成後に Discussion の URL を下の収集ログへ記録する。
2. 5サービスへ上記の経路で依頼文を送り、返答全文を取得する。サインインに失敗したら無言でリトライを繰り返さず、そのサービスはスキップして他を進め、失敗を収集ログに記録する。
3. 返答全文を ~/workspace/goals/paid-note-article-preparation/p39/research/discussion-<ai>.md（<ai> は chatgpt／claude／gemini／grok／qwen）に保存する。
4. 各返答を Discussion にコメント投稿し、投稿後に読み戻して確認する。収集ログを更新する。
5. repo への返答ファイル集約（products/1-1-documentary/10-fortnite/research/）はコネクタ経由で行うため、保存が済んだらメイン側へ引き継ぐ。

## 収集ログ

| サービス | 経路 | 状態 | 保存先 |
|---|---|---|---|
| Qwen | URL | 完了 | research/discussion-qwen.md |
| Grok | Googleサインイン後に再送 | 完了 | research/discussion-grok.md |
| ChatGPT | プロジェクト内チャット | 完了 | research/discussion-chatgpt.md |
| Gemini | URL | 完了 | research/discussion-gemini.md |
| Claude | Haiku・統合1回 | 完了 | research/discussion-claude.md |

Discussion URL: https://github.com/studio-chotto-bit/studio-chotto-bit/discussions/4
