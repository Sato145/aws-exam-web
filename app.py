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
            },
            # セキュリティ関連追加問題
            {
                "id": 21,
                "question": "AWS Key Management Service (KMS)の主な用途はどれか。",
                "choices": [
                    "ネットワークアクセスの制御",
                    "暗号化キーの管理",
                    "ユーザー認証",
                    "ログの監査"
                ],
                "answer": 1,
                "explanation": "KMSは暗号化キーの作成、管理、使用を行うマネージドサービスで、データの暗号化に使用されます。"
            },
            {
                "id": 22,
                "question": "AWS CloudTrailの主な機能はどれか。",
                "choices": [
                    "パフォーマンス監視",
                    "API呼び出しのログ記録",
                    "コスト分析",
                    "セキュリティグループの管理"
                ],
                "answer": 1,
                "explanation": "CloudTrailはAWSアカウント内のAPI呼び出しを記録し、監査とコンプライアンスのためのログを提供します。"
            },
            # コスト管理
            {
                "id": 23,
                "question": "AWS Cost Explorerで実行できない機能はどれか。",
                "choices": [
                    "過去のコスト分析",
                    "将来のコスト予測",
                    "リアルタイムのリソース使用量監視",
                    "サービス別コスト内訳"
                ],
                "answer": 2,
                "explanation": "Cost Explorerはコスト分析ツールで、リアルタイム監視はCloudWatchの機能です。"
            },
            {
                "id": 24,
                "question": "AWS Budgetsの主な機能はどれか。",
                "choices": [
                    "自動的なリソースの削除",
                    "コスト予算の設定とアラート",
                    "パフォーマンスの最適化",
                    "セキュリティ脆弱性の検出"
                ],
                "answer": 1,
                "explanation": "AWS Budgetsはコストや使用量の予算を設定し、閾値を超えた場合にアラートを送信する機能を提供します。"
            },
            # サポートプラン
            {
                "id": 25,
                "question": "AWS Supportプランで、24時間365日の電話サポートが含まれる最も低いプランはどれか。",
                "choices": [
                    "Basic",
                    "Developer",
                    "Business",
                    "Enterprise"
                ],
                "answer": 2,
                "explanation": "Businessプランから24時間365日の電話、チャット、メールサポートが利用可能になります。"
            },
            # 追加のEC2・ストレージ問題
            {
                "id": 26,
                "question": "Amazon EBSボリュームタイプで、最高のIOPSパフォーマンスを提供するものはどれか。",
                "choices": [
                    "gp2 (汎用SSD)",
                    "gp3 (汎用SSD)",
                    "io1 (プロビジョンドIOPS SSD)",
                    "st1 (スループット最適化HDD)"
                ],
                "answer": 2,
                "explanation": "io1ボリュームは最大64,000 IOPSまでプロビジョニング可能で、最高のIOPSパフォーマンスを提供します。"
            },
            {
                "id": 27,
                "question": "AWS Elastic Beanstalkの説明として最も適切なものはどれか。",
                "choices": [
                    "コンテナオーケストレーションサービス",
                    "アプリケーションデプロイメントサービス",
                    "データベース管理サービス",
                    "ネットワーク管理サービス"
                ],
                "answer": 1,
                "explanation": "Elastic Beanstalkは、Webアプリケーションやサービスのデプロイと管理を簡素化するPaaSサービスです。"
            },
            {
                "id": 28,
                "question": "Amazon CloudFormationの主な利点はどれか。",
                "choices": [
                    "手動でのリソース管理",
                    "Infrastructure as Code (IaC)",
                    "リアルタイム監視",
                    "データベースクエリ最適化"
                ],
                "answer": 1,
                "explanation": "CloudFormationはInfrastructure as Codeを実現し、AWSリソースをテンプレートで定義・管理できます。"
            },
            {
                "id": 29,
                "question": "Amazon ECSとEKSの主な違いはどれか。",
                "choices": [
                    "ECSはAWS独自、EKSはKubernetes",
                    "ECSはKubernetes、EKSはAWS独自",
                    "両方ともKubernetes",
                    "両方ともAWS独自"
                ],
                "answer": 0,
                "explanation": "ECS（Elastic Container Service）はAWS独自のコンテナオーケストレーション、EKS（Elastic Kubernetes Service）はマネージドKubernetesサービスです。"
            },
            {
                "id": 30,
                "question": "AWS Fargateの特徴として正しいものはどれか。",
                "choices": [
                    "EC2インスタンスの管理が必要",
                    "サーバーレスコンテナ実行環境",
                    "オンプレミス専用サービス",
                    "データベース専用サービス"
                ],
                "answer": 1,
                "explanation": "Fargateはサーバーレスコンテナ実行環境で、インフラ管理なしでコンテナを実行できます。"
            },
            # 追加のS3・ストレージ問題
            {
                "id": 31,
                "question": "Amazon S3の暗号化オプションで、顧客管理キーを使用するものはどれか。",
                "choices": [
                    "SSE-S3",
                    "SSE-KMS",
                    "SSE-C",
                    "すべて該当する"
                ],
                "answer": 2,
                "explanation": "SSE-C (Server-Side Encryption with Customer-Provided Keys)では、顧客が暗号化キーを提供・管理します。"
            },
            {
                "id": 32,
                "question": "AWS Global Infrastructureの構成要素として正しくないものはどれか。",
                "choices": [
                    "リージョン",
                    "アベイラビリティゾーン",
                    "エッジロケーション",
                    "データセンタークラスター"
                ],
                "answer": 3,
                "explanation": "AWSのグローバルインフラは、リージョン、アベイラビリティゾーン、エッジロケーションで構成されます。データセンタークラスターは正式な構成要素ではありません。"
            },
            {
                "id": 33,
                "question": "Amazon CloudWatchのカスタムメトリクスについて正しい説明はどれか。",
                "choices": [
                    "無料で無制限に作成できる",
                    "AWSサービスのメトリクスのみ対象",
                    "アプリケーション固有のメトリクスを作成可能",
                    "1分間隔でのみ送信可能"
                ],
                "answer": 2,
                "explanation": "CloudWatchカスタムメトリクスでは、アプリケーション固有のメトリクスを作成・送信できます。料金は発生し、様々な間隔で送信可能です。"
            },
            {
                "id": 34,
                "question": "AWS Trusted Advisorの機能として含まれないものはどれか。",
                "choices": [
                    "コスト最適化の推奨事項",
                    "セキュリティの推奨事項",
                    "パフォーマンスの推奨事項",
                    "アプリケーションコードの脆弱性検査"
                ],
                "answer": 3,
                "explanation": "Trusted Advisorはインフラレベルの推奨事項を提供しますが、アプリケーションコードの脆弱性検査は行いません。"
            },
            {
                "id": 35,
                "question": "Amazon RDSの Multi-AZ配置の主な目的はどれか。",
                "choices": [
                    "読み取りパフォーマンスの向上",
                    "高可用性の実現",
                    "コストの削減",
                    "ストレージ容量の拡張"
                ],
                "answer": 1,
                "explanation": "Multi-AZ配置は、プライマリDBインスタンスに障害が発生した場合の自動フェイルオーバーにより高可用性を実現します。"
            },
            {
                "id": 36,
                "question": "AWS Lambda関数の実行時間制限はどれか。",
                "choices": [
                    "5分",
                    "10分",
                    "15分",
                    "30分"
                ],
                "answer": 2,
                "explanation": "AWS Lambda関数の最大実行時間は15分です。それ以上の処理が必要な場合は他のサービスを検討する必要があります。"
            },
            {
                "id": 37,
                "question": "Amazon VPCのデフォルトセキュリティグループの特徴はどれか。",
                "choices": [
                    "すべてのインバウンドトラフィックを許可",
                    "同じセキュリティグループ内のインスタンス間通信を許可",
                    "HTTPとHTTPSのみを許可",
                    "SSH接続のみを許可"
                ],
                "answer": 1,
                "explanation": "デフォルトセキュリティグループは、同じセキュリティグループに属するインスタンス間の通信を許可し、すべてのアウトバウンドトラフィックを許可します。"
            },
            {
                "id": 38,
                "question": "AWS Config サービスの主な機能はどれか。",
                "choices": [
                    "パフォーマンス監視",
                    "リソース設定の記録と監査",
                    "コスト分析",
                    "セキュリティ脅威の検出"
                ],
                "answer": 1,
                "explanation": "AWS Configは、AWSリソースの設定変更を記録・追跡し、コンプライアンス監査をサポートするサービスです。"
            },
            {
                "id": 39,
                "question": "Amazon ElastiCacheでサポートされているキャッシュエンジンはどれか。",
                "choices": [
                    "RedisとMemcached",
                    "RedisとMongoDB",
                    "MemcachedとCassandra",
                    "RedisとDynamoDB"
                ],
                "answer": 0,
                "explanation": "Amazon ElastiCacheは、RedisとMemcachedの2つのオープンソースインメモリキャッシュエンジンをサポートしています。"
            },
            {
                "id": 40,
                "question": "AWS Organizations の主な利点として最も適切でないものはどれか。",
                "choices": [
                    "複数アカウントの一元管理",
                    "統合請求",
                    "サービス制御ポリシー (SCP)",
                    "アプリケーションの自動デプロイ"
                ],
                "answer": 3,
                "explanation": "AWS Organizationsは複数のAWSアカウントを管理するサービスで、アプリケーションの自動デプロイ機能は提供していません。"
            },
            # 追加のネットワーキング・API問題
            {
                "id": 41,
                "question": "Amazon API Gatewayの説明として正しいものはどれか。",
                "choices": [
                    "データベース接続サービス",
                    "RESTful APIの作成・管理サービス",
                    "ファイル転送サービス",
                    "メール送信サービス"
                ],
                "answer": 1,
                "explanation": "API GatewayはRESTful APIやWebSocket APIの作成、デプロイ、管理を行うフルマネージドサービスです。"
            },
            {
                "id": 42,
                "question": "AWS CloudFormationテンプレートの形式として正しいものはどれか。",
                "choices": [
                    "JSONまたはYAML",
                    "XMLまたはJSON",
                    "YAMLまたはXML",
                    "JSONのみ"
                ],
                "answer": 0,
                "explanation": "CloudFormationテンプレートは、JSON形式またはYAML形式で記述できます。"
            },
            {
                "id": 43,
                "question": "Amazon SQSの可視性タイムアウトの説明として正しいものはどれか。",
                "choices": [
                    "メッセージの保持期間",
                    "メッセージが他のコンシューマーから見えなくなる時間",
                    "キューの作成時間",
                    "メッセージの最大サイズ"
                ],
                "answer": 1,
                "explanation": "可視性タイムアウトは、メッセージが受信された後、他のコンシューマーから見えなくなる時間を指します。"
            },
            {
                "id": 44,
                "question": "AWS Direct Connectの主な利点はどれか。",
                "choices": [
                    "インターネット経由の暗号化通信",
                    "専用ネットワーク接続による安定した通信",
                    "無料のデータ転送",
                    "自動的なバックアップ"
                ],
                "answer": 1,
                "explanation": "Direct Connectは、オンプレミスからAWSへの専用ネットワーク接続を提供し、安定した帯域幅と低レイテンシを実現します。"
            },
            {
                "id": 45,
                "question": "Amazon Redshiftの説明として最も適切なものはどれか。",
                "choices": [
                    "NoSQLデータベース",
                    "データウェアハウスサービス",
                    "ファイルストレージサービス",
                    "メッセージキューサービス"
                ],
                "answer": 1,
                "explanation": "Amazon Redshiftは、ペタバイト規模のデータ分析に最適化されたフルマネージドデータウェアハウスサービスです。"
            },
            # 追加のセキュリティ・管理問題
            {
                "id": 46,
                "question": "AWS WAF (Web Application Firewall)の主な機能はどれか。",
                "choices": [
                    "データベースの暗号化",
                    "Webアプリケーションの脆弱性攻撃からの保護",
                    "ネットワーク帯域幅の制御",
                    "サーバーの自動スケーリング"
                ],
                "answer": 1,
                "explanation": "AWS WAFは、SQLインジェクション、クロスサイトスクリプティングなどのWebアプリケーション攻撃からの保護を提供します。"
            },
            {
                "id": 47,
                "question": "Amazon ECS (Elastic Container Service)でサポートされている起動タイプはどれか。",
                "choices": [
                    "EC2とFargate",
                    "EC2とLambda",
                    "FargateとLambda",
                    "EC2のみ"
                ],
                "answer": 0,
                "explanation": "ECSは、EC2起動タイプ（インスタンス管理あり）とFargate起動タイプ（サーバーレス）の2つをサポートしています。"
            },
            {
                "id": 48,
                "question": "AWS Systems Manager Parameter Storeの主な用途はどれか。",
                "choices": [
                    "ログファイルの保存",
                    "設定データと機密情報の安全な保存",
                    "バックアップファイルの管理",
                    "メトリクスデータの収集"
                ],
                "answer": 1,
                "explanation": "Parameter Storeは、設定データ、パスワード、データベース文字列などの機密情報を安全に保存・管理するサービスです。"
            },
            {
                "id": 49,
                "question": "Amazon CloudWatch Logsの保持期間設定について正しいものはどれか。",
                "choices": [
                    "最大1年間",
                    "最大5年間",
                    "最大10年間",
                    "無期限に設定可能"
                ],
                "answer": 3,
                "explanation": "CloudWatch Logsでは、ログの保持期間を1日から無期限まで設定できます。"
            },
            {
                "id": 50,
                "question": "AWS Certificate Manager (ACM)で提供される証明書の特徴はどれか。",
                "choices": [
                    "有料のSSL/TLS証明書",
                    "無料のSSL/TLS証明書",
                    "コード署名証明書のみ",
                    "メール暗号化証明書のみ"
                ],
                "answer": 1,
                "explanation": "ACMは、AWSサービスで使用するSSL/TLS証明書を無料で提供し、自動更新も行います。"
            },
            # 追加の高度なサービス問題
            {
                "id": 51,
                "question": "Amazon S3 Transfer Accelerationの仕組みはどれか。",
                "choices": [
                    "データ圧縮による高速化",
                    "CloudFrontエッジロケーションを利用した高速化",
                    "専用回線による高速化",
                    "マルチパート アップロードによる高速化"
                ],
                "answer": 1,
                "explanation": "S3 Transfer AccelerationはCloudFrontのエッジロケーションを利用して、世界中からS3への転送を高速化します。"
            },
            {
                "id": 52,
                "question": "AWS Shieldの説明として正しいものはどれか。",
                "choices": [
                    "データ暗号化サービス",
                    "DDoS攻撃からの保護サービス",
                    "ウイルス対策サービス",
                    "ファイアウォールサービス"
                ],
                "answer": 1,
                "explanation": "AWS ShieldはDDoS攻撃からAWSリソースを保護するマネージドサービスで、StandardとAdvancedの2つのレベルがあります。"
            },
            {
                "id": 53,
                "question": "Amazon EBSスナップショットの特徴として正しいものはどれか。",
                "choices": [
                    "リアルタイムでの同期バックアップ",
                    "増分バックアップ",
                    "完全バックアップのみ",
                    "自動削除機能なし"
                ],
                "answer": 1,
                "explanation": "EBSスナップショットは増分バックアップで、最初のスナップショット後は変更された部分のみが保存されます。"
            },
            {
                "id": 54,
                "question": "AWS Batch サービスの主な用途はどれか。",
                "choices": [
                    "リアルタイムデータ処理",
                    "バッチコンピューティングジョブの実行",
                    "Webアプリケーションのホスティング",
                    "データベースの管理"
                ],
                "answer": 1,
                "explanation": "AWS Batchは、数十万件のバッチコンピューティングジョブを効率的に実行するフルマネージドサービスです。"
            },
            {
                "id": 55,
                "question": "Amazon Inspector の機能はどれか。",
                "choices": [
                    "ネットワークパフォーマンスの監視",
                    "アプリケーションのセキュリティ評価",
                    "コストの最適化",
                    "データベースのクエリ最適化"
                ],
                "answer": 1,
                "explanation": "Amazon Inspectorは、EC2インスタンスとコンテナイメージのセキュリティ脆弱性を自動的に評価するサービスです。"
            },
            {
                "id": 56,
                "question": "AWS X-Ray の主な機能はどれか。",
                "choices": [
                    "分散アプリケーションのトレーシング",
                    "データベースのバックアップ",
                    "ネットワークの監視",
                    "コストの分析"
                ],
                "answer": 0,
                "explanation": "AWS X-Rayは、分散アプリケーションのリクエストをトレースし、パフォーマンスのボトルネックを特定するサービスです。"
            },
            {
                "id": 57,
                "question": "Amazon Kinesis Data Streamsの説明として正しいものはどれか。",
                "choices": [
                    "バッチデータ処理サービス",
                    "リアルタイムデータストリーミングサービス",
                    "ファイル転送サービス",
                    "データベース同期サービス"
                ],
                "answer": 1,
                "explanation": "Kinesis Data Streamsは、リアルタイムでストリーミングデータを収集・処理するサービスです。"
            },
            {
                "id": 58,
                "question": "AWS CodeCommit の説明として正しいものはどれか。",
                "choices": [
                    "継続的インテグレーションサービス",
                    "Gitリポジトリホスティングサービス",
                    "アプリケーションデプロイサービス",
                    "コード品質分析サービス"
                ],
                "answer": 1,
                "explanation": "CodeCommitは、プライベートGitリポジトリをホストするフルマネージドソースコントロールサービスです。"
            },
            {
                "id": 59,
                "question": "Amazon EMR (Elastic MapReduce)の主な用途はどれか。",
                "choices": [
                    "Webアプリケーションのホスティング",
                    "ビッグデータ処理",
                    "データベースの管理",
                    "ファイルの同期"
                ],
                "answer": 1,
                "explanation": "EMRは、Apache Spark、Hadoop、HBaseなどのビッグデータフレームワークを使用した大規模データ処理を行うサービスです。"
            },
            {
                "id": 60,
                "question": "AWS Secrets Manager の主な機能はどれか。",
                "choices": [
                    "ログファイルの管理",
                    "機密情報の安全な保存と自動ローテーション",
                    "ネットワーク設定の管理",
                    "バックアップの管理"
                ],
                "answer": 1,
                "explanation": "Secrets Managerは、データベースの認証情報やAPIキーなどの機密情報を安全に保存し、自動ローテーション機能を提供します。"
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