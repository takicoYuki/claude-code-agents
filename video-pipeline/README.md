# 動画制作エージェント一式

## 置き方
このフォルダごと任意の場所に置く。
その中でターミナルを開いて `claude` を起動する。

## 中身
- `CLAUDE.md` … 司令塔の指示（工程の順番）
- `.claude/agents/` … 担当エージェント6人
  - scenario-writer（シナリオ）／character-designer（キャラ）／serifu-writer（セリフ）
  - script-checker（台本チェック）／veo-prompt-writer（Veoプロンプト）／video-checker（動画チェック）
- `.claude/skills/video-rules/` … 全員共通のルール
- `.claude/skills/frame-check/` … 動画から確認用の画像を書き出す道具（ffmpegが必要）
- `work/` … 動画ごとの作業フォルダがここにできる

## 使い方
1. `/agents` で6人が表示されるか確認
2. 例：「一人建築シリーズで、雪の中にかまくらを作る動画を作って」
3. Veoプロンプトができたら止まるので、Flowで生成して `work/<動画名>/video/` にmp4を入れる
4. 「動画入れたのでチェックして」と伝える
5. 結果を見て、自分で承認してからアップ

## 直したいとき
- ルールを足す → `video-rules/SKILL.md` に1行追加
- 担当のクセを直す → その担当の `.md` だけ編集
