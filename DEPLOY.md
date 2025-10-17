# AWS試験対策アプリ - デプロイ手順

## 🚀 GitHubとRenderでのデプロイ方法

### 1. GitHubリポジトリの作成

#### ローカルでGitリポジトリを初期化
```bash
cd aws-exam-web
git init
git add .
git commit -m "Initial commit: AWS Certified Cloud Practitioner exam app"
```

#### GitHubでリポジトリを作成
1. [GitHub](https://github.com)にログイン
2. 右上の「+」→「New repository」をクリック
3. リポジトリ名: `aws-exam-web` (または任意の名前)
4. 説明: `AWS Certified Cloud Practitioner exam practice web app`
5. Public または Private を選択
6. 「Create repository」をクリック

#### ローカルリポジトリをGitHubにプッシュ
```bash
# GitHubのリポジトリURLを設定（YOUR_USERNAMEを実際のユーザー名に変更）
git remote add origin https://github.com/YOUR_USERNAME/aws-exam-web.git
git branch -M main
git push -u origin main
```

### 2. Renderでのデプロイ

#### Renderアカウントの作成・ログイン
1. [Render](https://render.com)にアクセス
2. GitHubアカウントでサインアップ/ログイン

#### Web Serviceの作成
1. ダッシュボードで「New +」→「Web Service」をクリック
2. 「Connect a repository」でGitHubリポジトリを選択
3. 設定項目を入力：
   - **Name**: `aws-exam-web` (または任意)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn -c gunicorn.conf.py app:app`
   - **Plan**: `Free` (無料プラン)

#### 環境変数の設定（オプション）
- 必要に応じて環境変数を設定
- 通常は設定不要（デフォルト設定で動作）

#### デプロイの実行
1. 「Create Web Service」をクリック
2. 自動的にビルド・デプロイが開始
3. 数分後にアプリケーションが利用可能に

### 3. デプロイ後の確認

#### アクセスURL
- Renderが自動生成するURL: `https://aws-exam-web-xxxx.onrender.com`
- カスタムドメインも設定可能

#### 動作確認
- ホームページが正常に表示されるか
- 問題練習機能が動作するか
- 成績管理機能が動作するか

### 4. 更新・再デプロイ

#### コード更新時
```bash
git add .
git commit -m "Update: 機能追加や修正内容"
git push origin main
```

- GitHubにプッシュすると自動的にRenderで再デプロイされます

### 5. トラブルシューティング

#### よくある問題と解決方法

**ビルドエラー**
- `requirements.txt`の依存関係を確認
- Pythonバージョンの互換性を確認

**起動エラー**
- `gunicorn.conf.py`の設定を確認
- ポート設定（環境変数PORT）を確認

**テンプレートエラー**
- `templates/`フォルダが正しく含まれているか確認
- Jinjaテンプレートの構文エラーを確認

#### ログの確認
- Renderダッシュボードの「Logs」タブでエラーログを確認

### 6. 本番環境での最適化

#### パフォーマンス向上
- 静的ファイルのCDN配信
- データベースキャッシュの実装
- Gunicornワーカー数の調整

#### セキュリティ強化
- HTTPS強制リダイレクト
- セキュリティヘッダーの追加
- 入力値検証の強化

## 📱 PWA対応（スマホアプリ化）

### iPhoneでの使用方法
1. Safariでアプリにアクセス
2. 画面下部の共有ボタンをタップ
3. 「ホーム画面に追加」を選択
4. アプリ名を設定して「追加」

### Androidでの使用方法
1. Chromeでアプリにアクセス
2. メニューから「ホーム画面に追加」を選択
3. アプリ名を確認して「追加」

## 🎯 成功のポイント

- **継続的な学習**: 毎日少しずつでも問題を解く
- **弱点の把握**: 成績画面で苦手分野を特定
- **解説の活用**: 間違えた問題の解説をしっかり読む
- **実践的理解**: AWSコンソールで実際にサービスを触ってみる

合格目標: **70%以上**（1000点満点中700点以上）
頑張って合格を目指しましょう！🎉