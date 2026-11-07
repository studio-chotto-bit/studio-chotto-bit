# P38 DeepReview 再実施レポート（2026-11-07）— 未実施・枠切れのため中止

- 対象：P38『ポケモンGOは、何を作っていたのか』（統合ファイル `combined-all.md`、ブラッシュアップ済み最新版 17,186字）
- 実施日：2026-11-07 19:14〜19:38 JST
- 結果：**レビューは開始できなかった。個人・事業用の両アカウントで週の無料枠切れ。** レポート本文・指摘件数・結果ページURLはなし。

## 経緯

- 19:14、個人 Google アカウント tsoulala@gmail.com でセッションが生きている状態で https://research.google/deepreview を開いた（ログイン画面なし）。
- 前回の旧版レビュー（結果ページ https://research.google/deepreview/documents/7cc9c6bd-7c32-4c77-afdd-930879ddd11a、Major 2・Minor 5・Suggestion 1＝計8件）を確認し、再レビューしないよう区別した。
- 付与した最新版 combined-all.md（17,186字）をファイルそのもののアップロード機能で新規投入。アップロードは成功し、「Your documents」最上段に combined-all.md（Nov 7, 2026／Not started）の新規行が追加された。転記・貼り付け・要約はしていない。
- 個人アカウントで「Upload Document for Review」を押すと「You have exhausted your quota for the week (2 free reviews per week). Attach a Gemini API key to proceed.」と表示され、開始できなかった。
- 指示のフォールバックどおり事業用 Google アカウント studio.chotto.bit@gmail.com に切り替えた（全アカウントからサインアウト後、事業用でサインイン完了。reCAPTCHA はチェックボックス1回で通過、パスワード入力で完了、2段階認証コードは求められず。myaccount.google.com で表示名「bit chotto」、メールアドレス studio.chotto.bit@gmail.com、他にサインイン中のアカウントなしを確認）。
- しかし事業用のみでサインインした状態でも DeepReview の「Your documents」一覧は個人アカウント時代と同一の内容のままで、19:15に新規アップロードした combined-all.md（Not started）に「Start Review」を押しても同じ枠切れメッセージが表示され、レビューは開始できなかった。DeepReview の枠は、この環境では Google アカウントの切り替えだけでは切り替わらない（ブラウザ／DeepReview 独自セッションに紐づいているように見える）。

## 未取得の項目（レビュー未実施のため）

- 使用アカウント：個人 tsoulala@gmail.com で枠切れを確認後、事業用 studio.chotto.bit@gmail.com でも枠切れを確認（レビュー開始に至らず）
- 結果ページURL：なし（新規レビューは開始されていない）
- 指摘件数（Major／Minor／Suggestion）：なし
- 「View as Report」表示のレポート全文：なし
- 前回指摘8件の解消／残存、およびブラッシュアップ追加記述（台帳3のWayfarer／データ供給の段落、グラス判定のOS競合の段落、確度分類の書き換え）への新たな指摘の有無：未確認

## 補足・注意点

- 新規アップロードした combined-all.md は DeepReview 上に「Not started」のまま残っている。枠が回復すれば、再アップロードなしに開始できる可能性がある。旧版の完了済みレビューは再レビューしていない。
- 切り替え作業の過程で、個人アカウント tsoulala@gmail.com はこのブラウザからサインアウトされた状態になっている。個人アカウントを再度使う場合は再サインインが必要。
- 原稿の修正、note 下書き作成、公開・価格設定などの外部公開行為は一切行っていない。
- 次の実施方法の候補：週の無料枠の回復を待つか、Gemini API キーを添付して実施する（API キーは本作業では付与・指示されていないため未実施）。いずれもオーナーの判断が必要。
- 事業用 repo（products/38-pokemon-go/research/）への集約は行っていない。レビュー結果が存在しないため、集約する成果物がない。

## 枠の状況の整理

- 個人アカウント：本日 17:53〜の前回実施開始時点で「1 free review left of 2 free reviews per week」表示で、その1件を消費したため今週分は使い切り。枠切れは想定内。
- 事業用アカウント：同じブラウザでアカウントを切り替えても DeepReview 側の枠表示・文書一覧が変わらなかったため、事業用アカウント単独の枠が本当に切れているのか、DeepReview のセッションが個人アカウントの枠状態を引き継いでいるのかは、この結果だけでは切り分けできていない。次回は別プロファイル／別セッションでの確認が要る可能性がある。
