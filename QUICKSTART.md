# 🚀 クイックスタート - GitHubとRenderデプロイ

## 📋 必要な準備
- GitHubアカウント
- Renderアカウント（GitHubでサインアップ可能）

## ⚡ 5分でデプロイ

### 1️⃣ GitHubリポジトリ作成
```bash
# プロジェクトフォルダに移動
cd aws-exam-web

# Gitリポジトリ初期化
git init
git add .
git commit -m "🎉 AWS試験対策アプリ初回コミット"

# GitHubでリポジトリ作成後、以下を実行
# （YOUR_USERNAMEを実際のユーザー名に変更）
git remote add origin https://github.com/YOUR_USERNAME/aws-exam-web.git
git branch -M main
git push -u origin main
```

### 2️⃣ Renderでデプロイ
1. **[Render](https://render.com)** にアクセス
2. **GitHubでサインアップ/ログイン**
3. **「New +」→「Web Service」**
4. **GitHubリポジトリを選択**
5. **設定項目**:
   - Name: `aws-exam-web`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn -c gunicorn.conf.py app:app`
6. **「Create Web Service」をクリック**

### 3️⃣ 完了！
- 数分後にアプリが利用可能
- URL: `https://aws-exam-web-xxxx.onrender.com`

## 📱 スマホアプリ化

### iPhone
1. Safariでアクセス
2. 共有ボタン → 「ホーム画面に追加」

### Android  
1. Chromeでアクセス
2. メニュー → 「ホーム画面に追加」

## 🔄 更新方法
```bash
# コード修正後
git add .
git commit -m "✨ 機能追加"
git push origin main
# → 自動的に再デプロイ
```

## 🎯 学習のコツ
- **毎日継続**: 10-15分でも効果的
- **弱点克服**: 成績画面で苦手分野を特定
- **解説重視**: 間違えた問題の解説を熟読
- **実践学習**: AWSコンソールで実際に操作

**目標**: 70%以上で合格！頑張りましょう！🏆