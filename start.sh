#!/bin/bash

# AWS試験対策アプリ起動スクリプト

echo "AWS Certified Cloud Practitioner 試験対策アプリを起動します..."

# 仮想環境の確認
if [ ! -d ".venv" ]; then
    echo "仮想環境を作成します..."
    python3 -m venv .venv
fi

# 仮想環境をアクティベート
source .venv/bin/activate

# 依存関係をインストール
echo "依存関係をインストールします..."
pip install -r requirements.txt

# アプリケーションを起動
echo "アプリケーションを起動します..."
echo "ブラウザで http://localhost:8080 にアクセスしてください"
python3 app.py