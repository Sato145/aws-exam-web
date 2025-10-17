#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AWS Certified Cloud Practitioner試験対策 Webアプリケーション
"""

from flask import Flask, render_template, request, jsonify, session
import random
import json
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'aws_exam_practice_secret_key'

class AWSExamData:
    def __init__(self):
        self.questions = [
            # クラウドコンピューティングの基本概念
            {
                "id": 1,
                "question": "クラウドコンピューティングの主要な利点として最も適切でないものはどれか。",
                "choices": [
                    "初期投資コストの削減",
                    "スケーラビリティの向上",
                    "データの完全な物理的制御",
                    "運用コストの最適化"
                ],
                "answer": 2,
                "explanation": "クラウドでは物理的なインフラは提供者が管理するため、ユーザーはデータの完全な物理的制御を持ちません。これはクラウドの特性であり、利点ではありません。"
            },
            {
                "id": 2,
                "question": "AWS Well-Architected Frameworkの5つの柱に含まれないものはどれか。",
                "choices": [
                    "運用上の優秀性",
                    "セキュリティ",
                    "データベース最適化",
                    "コスト最適化"
                ],
                "answer": 2,
                "explanation": "AWS Well-Architected Frameworkの5つの柱は、運用上の優秀性、セキュリティ、信頼性、パフォーマンス効率、コスト最適化です。"
            },
            {
                "id": 3,
                "question": "AWSの責任共有モデルにおいて、顧客の責任に含まれるものはどれか。",
                "choices": [
                    "データセンターの物理的セキュリティ",
                    "ハードウェアの保守",
                    "オペレーティングシステムのパッチ適用",
                    "ネットワークインフラの管理"
                ],
                "answer": 2,
                "explanation": "責任共有モデルでは、EC2インスタンスのOSパッチ適用は顧客の責任です。AWSはインフラを、顧客はその上で動作するものを管理します。"
            },
            # EC2 (Elastic Compute Cloud)
            {
                "id": 4,
                "question": "Amazon EC2インスタンスタイプの選択において、CPUパフォーマンスを最優先する場合に適したファミリーはどれか。",
                "choices": [
                    "t3 (汎用バーストパフォーマンス)",
                    "c5 (コンピューティング最適化)",
                    "r5 (メモリ最適化)",
                    "i3 (ストレージ最適化)"
                ],
                "answer": 1,
                "explanation": "c5ファミリーはコンピューティング最適化インスタンスで、高いCPUパフォーマンスが必要なワークロードに適しています。"
            },
            {
                "id": 5,
                "question": "EC2インスタンスの購入オプションで、最も低コストで利用できるが可用性が保証されないものはどれか。",
                "choices": [
                    "オンデマンドインスタンス",
                    "リザーブドインスタンス",
                    "スポットインスタンス",
                    "専用ホスト"
                ],
                "answer": 2,
                "explanation": "スポットインスタンスは余剰キャパシティを利用するため最も安価ですが、需要に応じて中断される可能性があります。"
            },
            # S3 (Simple Storage Service)
            {
                "id": 6,
                "question": "Amazon S3のストレージクラスで、アクセス頻度が低く、取得時間に柔軟性があるデータに最適なものはどれか。",
                "choices": [
                    "S3 Standard",
                    "S3 Standard-IA",
                    "S3 Glacier",
                    "S3 One Zone-IA"
                ],
                "answer": 2,
                "explanation": "S3 Glacierは長期アーカイブ用で、アクセス頻度が低く、取得に数分から数時間かかることを許容できるデータに適しています。"
            },
            {
                "id": 7,
                "question": "S3バケットのデフォルトのアクセス権限はどれか。",
                "choices": [
                    "パブリック読み取り可能",
                    "パブリック読み書き可能",
                    "プライベート（所有者のみアクセス可能）",
                    "認証されたユーザーのみアクセス可能"
                ],
                "answer": 2,
                "explanation": "S3バケットはデフォルトでプライベートに設定され、バケット所有者のみがアクセス可能です。"
            },
            # RDS (Relational Database Service)
            {
                "id": 8,
                "question": "Amazon RDSで提供されていないデータベースエンジンはどれか。",
                "choices": [
                    "MySQL",
                    "PostgreSQL",
                    "MongoDB",
                    "Oracle"
                ],
                "answer": 2,
                "explanation": "MongoDBはNoSQLデータベースで、RDSではサポートされていません。MongoDBを使用する場合はAmazon DocumentDBを利用します。"
            },
            {
                "id": 9,
                "question": "RDSの自動バックアップ機能について正しい説明はどれか。",
                "choices": [
                    "デフォルトで無効になっている",
                    "最大35日間保持可能",
                    "手動スナップショットと同じ機能",
                    "削除されたDBインスタンスのバックアップは永続的に保持される"
                ],
                "answer": 1,
                "explanation": "RDSの自動バックアップは最大35日間保持でき、ポイントインタイムリカバリが可能です。"
            },
            # VPC (Virtual Private Cloud)
            {
                "id": 10,
                "question": "VPCにおけるサブネットの説明として正しいものはどれか。",
                "choices": [
                    "サブネットは複数のアベイラビリティゾーンにまたがることができる",
                    "プライベートサブネットはインターネットゲートウェイに直接接続される",
                    "パブリックサブネットはインターネットゲートウェイへのルートを持つ",
                    "サブネットのCIDRブロックはVPCより大きくできる"
                ],
                "answer": 2,
                "explanation": "パブリックサブネットは、インターネットゲートウェイへのルートを持つルートテーブルに関連付けられたサブネットです。"
            },
            # IAM (Identity and Access Management)
            {
                "id": 11,
                "question": "IAMにおける最小権限の原則について正しい説明はどれか。",
                "choices": [
                    "すべてのユーザーに管理者権限を付与する",
                    "必要最小限の権限のみを付与する",
                    "デフォルトですべての権限を付与し、必要に応じて削除する",
                    "グループ権限は個別権限より優先される"
                ],
                "answer": 1,
                "explanation": "最小権限の原則では、ユーザーやサービスに必要最小限の権限のみを付与し、セキュリティリスクを最小化します。"
            },
            {
                "id": 12,
                "question": "IAMロールの主な用途として最も適切なものはどれか。",
                "choices": [
                    "長期的な認証情報の保存",
                    "AWSサービス間の一時的な権限付与",
                    "パスワードの暗号化",
                    "ネットワークアクセスの制御"
                ],
                "answer": 1,
                "explanation": "IAMロールは、AWSサービスやアプリケーションが他のAWSサービスにアクセスする際の一時的な権限付与に使用されます。"
            },
            # CloudWatch
            {
                "id": 13,
                "question": "Amazon CloudWatchの主な機能として含まれないものはどれか。",
                "choices": [
                    "メトリクスの監視",
                    "ログの収集と分析",
                    "アラームの設定",
                    "データベースのクエリ最適化"
                ],
                "answer": 3,
                "explanation": "CloudWatchは監視サービスで、メトリクス監視、ログ管理、アラーム機能を提供しますが、データベースクエリの最適化は行いません。"
            },
            # Auto Scaling
            {
                "id": 14,
                "question": "Auto Scalingグループの設定で必須となる項目はどれか。",
                "choices": [
                    "最大インスタンス数のみ",
                    "起動テンプレートまたは起動設定",
                    "ロードバランサーの設定",
                    "CloudWatchアラームの設定"
                ],
                "answer": 1,
                "explanation": "Auto Scalingグループを作成するには、インスタンスの起動方法を定義する起動テンプレートまたは起動設定が必須です。"
            },
            # Elastic Load Balancer
            {
                "id": 15,
                "question": "Application Load Balancer (ALB)の特徴として正しいものはどれか。",
                "choices": [
                    "レイヤー4（TCP/UDP）で動作する",
                    "静的IPアドレスを提供する",
                    "パスベースルーティングが可能",
                    "1つのアベイラビリティゾーンでのみ動作"
                ],
                "answer": 2,
                "explanation": "ALBはレイヤー7で動作し、URLパスやホストヘッダーに基づいたルーティングが可能です。"
            },
            # Route 53
            {
                "id": 16,
                "question": "Amazon Route 53のヘルスチェック機能の説明として正しいものはどれか。",
                "choices": [
                    "DNSクエリの応答時間のみを監視する",
                    "エンドポイントの可用性を監視し、障害時に自動的にトラフィックを迂回する",
                    "ドメイン名の有効期限のみを監視する",
                    "SSL証明書の有効性のみを確認する"
                ],
                "answer": 1,
                "explanation": "Route 53のヘルスチェックは、エンドポイントの健全性を監視し、障害を検出すると自動的にトラフィックを健全なエンドポイントに迂回します。"
            },
            # CloudFront
            {
                "id": 17,
                "question": "Amazon CloudFrontの主な利点として最も適切でないものはどれか。",
                "choices": [
                    "コンテンツ配信の高速化",
                    "DDoS攻撃からの保護",
                    "データベースクエリの高速化",
                    "グローバルなコンテンツ配信"
                ],
                "answer": 2,
                "explanation": "CloudFrontはCDN（Content Delivery Network）サービスで、静的・動的コンテンツの配信を高速化しますが、データベースクエリの高速化は行いません。"
            },
            # Lambda
            {
                "id": 18,
                "question": "AWS Lambdaの課金モデルについて正しい説明はどれか。",
                "choices": [
                    "インスタンスの起動時間に基づく",
                    "関数の実行回数と実行時間に基づく",
                    "メモリ使用量のみに基づく",
                    "月額固定料金"
                ],
                "answer": 1,
                "explanation": "Lambdaは関数の実行回数（リクエスト数）と実行時間（GB秒）に基づいて課金されるサーバーレスサービスです。"
            },
            # DynamoDB
            {
                "id": 19,
                "question": "Amazon DynamoDBの特徴として正しいものはどれか。",
                "choices": [
                    "SQLクエリをサポートする",
                    "NoSQLデータベースである",
                    "単一のアベイラビリティゾーンでのみ動作する",
                    "手動でのスケーリングが必要"
                ],
                "answer": 1,
                "explanation": "DynamoDBはフルマネージドNoSQLデータベースサービスで、自動スケーリングと高可用性を提供します。"
            },
            # SNS & SQS
            {
                "id": 20,
                "question": "Amazon SNSとSQSの主な違いはどれか。",
                "choices": [
                    "SNSはプッシュ型、SQSはプル型",
                    "SNSはプル型、SQSはプッシュ型",
                    "両方ともプッシュ型",
                    "両方ともプル型"
                ],
                "answer": 0,
                "explanation": "SNS（Simple Notification Service）はプッシュ型でメッセージを配信し、SQS（Simple Queue Service）はプル型でメッセージを取得します。"
            }
        ]

    def get_random_questions(self, count=10):
        """ランダムに問題を取得"""
        return random.sample(self.questions, min(count, len(self.questions)))

    def get_question_by_id(self, question_id):
        """IDで問題を取得"""
        for question in self.questions:
            if question["id"] == question_id:
                return question
        return None

# グローバルインスタンス
exam_data = AWSExamData()

@app.route('/')
def index():
    """メインページ"""
    return render_template('index.html')

@app.route('/exam')
def exam():
    """試験ページ"""
    count = request.args.get('count', 10, type=int)
    questions = exam_data.get_random_questions(count)
    return render_template('exam.html', questions=questions)

@app.route('/api/questions')
def api_questions():
    """問題取得API"""
    count = request.args.get('count', 10, type=int)
    questions = exam_data.get_random_questions(count)
    return jsonify(questions)

@app.route('/api/question/<int:question_id>')
def api_question(question_id):
    """個別問題取得API"""
    question = exam_data.get_question_by_id(question_id)
    if question:
        return jsonify(question)
    return jsonify({"error": "Question not found"}), 404

@app.route('/scores')
def scores():
    """成績ページ"""
    return render_template('scores.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)