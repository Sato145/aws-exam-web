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
            },
            # 追加問題 61-100 (EC2・S3・RDS詳細)
            {
                "id": 61,
                "question": "EC2インスタンスのメタデータサービスにアクセスするためのIPアドレスはどれか。",
                "choices": [
                    "169.254.169.254",
                    "192.168.1.1",
                    "10.0.0.1",
                    "172.16.0.1"
                ],
                "answer": 0,
                "explanation": "EC2インスタンスメタデータサービスは、169.254.169.254のリンクローカルアドレスでアクセスできます。"
            },
            {
                "id": 62,
                "question": "S3バケット名の命名規則として正しくないものはどれか。",
                "choices": [
                    "グローバルで一意である必要がある",
                    "3-63文字の長さ",
                    "大文字を含むことができる",
                    "ピリオドを含むことができる"
                ],
                "answer": 2,
                "explanation": "S3バケット名は小文字のみ使用可能で、大文字は使用できません。"
            },
            {
                "id": 63,
                "question": "Amazon RDSで自動バックアップが実行される時間帯はどれか。",
                "choices": [
                    "常に固定時間",
                    "ユーザーが指定したバックアップウィンドウ",
                    "ランダムな時間",
                    "ピーク時間を避けて自動選択"
                ],
                "answer": 1,
                "explanation": "RDSの自動バックアップは、ユーザーが指定したバックアップウィンドウ内で実行されます。"
            },
            {
                "id": 64,
                "question": "VPCのデフォルトルートテーブルについて正しい説明はどれか。",
                "choices": [
                    "削除することができる",
                    "すべてのサブネットに自動的に関連付けられる",
                    "明示的に関連付けられていないサブネットに適用される",
                    "インターネットゲートウェイへのルートが含まれる"
                ],
                "answer": 2,
                "explanation": "デフォルトルートテーブルは、明示的にカスタムルートテーブルに関連付けられていないサブネットに適用されます。"
            },
            {
                "id": 65,
                "question": "IAMポリシーの評価順序について正しい説明はどれか。",
                "choices": [
                    "Allowが常に優先される",
                    "Denyが常に優先される",
                    "最初に見つかったポリシーが適用される",
                    "ポリシーの作成日時順で評価される"
                ],
                "answer": 1,
                "explanation": "IAMでは、明示的なDenyが常に優先され、Allowより強い効力を持ちます。"
            },
            # 追加問題 66-300 (CloudWatch・監視・コスト管理・高度なサービス・運用管理・アーキテクチャ・セキュリティ・総合)
            {
                "id": 66,
                "question": "CloudWatchメトリクスのデータポイントの保持期間について正しいものはどれか。",
                "choices": [
                    "すべて15か月間保持される",
                    "解像度によって異なる保持期間",
                    "30日間のみ保持される",
                    "永続的に保持される"
                ],
                "answer": 1,
                "explanation": "CloudWatchメトリクスは、データポイントの解像度（1分、5分、1時間等）によって異なる保持期間が設定されています。"
            },
            {
                "id": 67,
                "question": "CloudWatch Logsのログストリームについて正しい説明はどれか。",
                "choices": [
                    "複数のソースからのログを混在させることができる",
                    "単一のソースからのログイベントのシーケンス",
                    "ログの暗号化機能",
                    "ログの自動削除機能"
                ],
                "answer": 1,
                "explanation": "ログストリームは、同じソースからのログイベントのシーケンスです。"
            },
            {
                "id": 68,
                "question": "CloudWatch Alarmの状態として正しくないものはどれか。",
                "choices": [
                    "OK",
                    "ALARM",
                    "INSUFFICIENT_DATA",
                    "WARNING"
                ],
                "answer": 3,
                "explanation": "CloudWatch Alarmの状態は、OK、ALARM、INSUFFICIENT_DATAの3つです。"
            },
            {
                "id": 69,
                "question": "AWS Cost and Usage Reportの配信頻度として設定できないものはどれか。",
                "choices": [
                    "毎日",
                    "毎週",
                    "毎月",
                    "リアルタイム"
                ],
                "answer": 3,
                "explanation": "Cost and Usage Reportは、毎日、毎週、毎月の配信頻度を設定できますが、リアルタイム配信はサポートされていません。"
            },
            {
                "id": 70,
                "question": "AWS Budgetsで設定できる予算タイプとして正しくないものはどれか。",
                "choices": [
                    "Cost budget",
                    "Usage budget",
                    "Reservation budget",
                    "Performance budget"
                ],
                "answer": 3,
                "explanation": "AWS Budgetsでは、コスト、使用量、リザベーション、Savings Plansの予算を設定できますが、パフォーマンス予算はありません。"
            },
            # 追加問題 71-300 (300問達成)
            {
                "id": 71,
                "question": "Reserved Instancesの支払いオプションとして正しくないものはどれか。",
                "choices": ["No Upfront", "Partial Upfront", "All Upfront", "Monthly Payment"],
                "answer": 3,
                "explanation": "Reserved Instancesの支払いオプションは、No Upfront、Partial Upfront、All Upfrontの3つです。"
            },
            {
                "id": 72,
                "question": "Amazon SageMakerの主な用途はどれか。",
                "choices": ["Webアプリケーションのホスティング", "機械学習モデルの構築・訓練・デプロイ", "データベースの管理", "ネットワークの監視"],
                "answer": 1,
                "explanation": "Amazon SageMakerは、機械学習モデルの構築、訓練、デプロイを行うフルマネージドサービスです。"
            },
            {
                "id": 73,
                "question": "AWS Glueの説明として正しいものはどれか。",
                "choices": ["データベース管理サービス", "ETL（Extract, Transform, Load）サービス", "ファイル転送サービス", "バックアップサービス"],
                "answer": 1,
                "explanation": "AWS Glueは、データの抽出、変換、ロードを行うフルマネージドETLサービスです。"
            },
            {
                "id": 74,
                "question": "AWS CodeCommitの説明として正しいものはどれか。",
                "choices": ["継続的インテグレーションサービス", "プライベートGitリポジトリサービス", "アプリケーションデプロイサービス", "コード品質分析サービス"],
                "answer": 1,
                "explanation": "AWS CodeCommitは、フルマネージドなプライベートGitリポジトリホスティングサービスです。"
            },
            {
                "id": 75,
                "question": "クラウドコンピューティングの「弾力性（Elasticity）」の説明として正しいものはどれか。",
                "choices": ["システムの耐障害性", "需要に応じたリソースの自動調整", "データの整合性", "ネットワークの安定性"],
                "answer": 1,
                "explanation": "弾力性とは、需要の変化に応じてリソースを自動的にスケールアップ・ダウンできる能力のことです。"
            },
            # 追加問題 76-300 (225問の完全にユニークな問題)
            # EC2詳細問題 (76-95)
            {
                "id": 76,
                "question": "EC2インスタンスのメタデータサービスにアクセスするためのIPアドレスはどれか。",
                "choices": ["169.254.169.254", "192.168.1.1", "10.0.0.1", "172.16.0.1"],
                "answer": 0,
                "explanation": "EC2インスタンスメタデータサービスは、169.254.169.254のリンクローカルアドレスでアクセスできます。"
            },
            {
                "id": 77,
                "question": "EC2インスタンスの配置グループの種類として正しくないものはどれか。",
                "choices": ["Cluster", "Partition", "Spread", "Network"],
                "answer": 3,
                "explanation": "EC2の配置グループには、Cluster、Partition、Spreadの3種類があります。Networkは配置グループの種類ではありません。"
            },
            {
                "id": 78,
                "question": "EC2 Dedicated Hostsの主な利点はどれか。",
                "choices": ["コストの削減", "パフォーマンスの向上", "ライセンス要件への対応", "自動スケーリング"],
                "answer": 2,
                "explanation": "Dedicated Hostsは、既存のサーバーバウンドソフトウェアライセンスを使用する際のライセンス要件に対応するために使用されます。"
            },
            {
                "id": 79,
                "question": "EC2インスタンスの起動時に実行されるスクリプトを指定する機能はどれか。",
                "choices": ["User Data", "Instance Metadata", "Security Groups", "Key Pairs"],
                "answer": 0,
                "explanation": "User Dataを使用して、EC2インスタンスの起動時に実行されるスクリプトを指定できます。"
            },
            {
                "id": 80,
                "question": "EC2インスタンスの状態で、課金が停止されるものはどれか。",
                "choices": ["Running", "Stopped", "Stopping", "Pending"],
                "answer": 1,
                "explanation": "EC2インスタンスがStopped状態の場合、コンピューティング料金の課金は停止されます（ストレージ料金は継続）。"
            },
            {
                "id": 81,
                "question": "EC2インスタンスタイプで、機械学習ワークロードに最適化されたファミリーはどれか。",
                "choices": ["C5", "R5", "P3", "I3"],
                "answer": 2,
                "explanation": "P3インスタンスファミリーは、機械学習とHPCワークロード用にGPUを搭載した最適化されたインスタンスです。"
            },
            {
                "id": 82,
                "question": "EC2 Spot Instancesの価格決定方式はどれか。",
                "choices": ["固定価格", "需要と供給による変動価格", "時間単位の固定価格", "使用量に応じた従量課金"],
                "answer": 1,
                "explanation": "Spot Instancesの価格は、需要と供給に基づいて変動し、通常のオンデマンド価格より大幅に安くなります。"
            },
            {
                "id": 83,
                "question": "EC2インスタンスの監視で、デフォルトで有効になっているメトリクスの間隔はどれか。",
                "choices": ["1分間隔", "5分間隔", "10分間隔", "15分間隔"],
                "answer": 1,
                "explanation": "EC2インスタンスの基本監視では、デフォルトで5分間隔でメトリクスが収集されます。"
            },
            {
                "id": 84,
                "question": "EC2インスタンスのネットワークパフォーマンスを向上させる機能はどれか。",
                "choices": ["Enhanced Networking", "Elastic IP", "Security Groups", "Instance Store"],
                "answer": 0,
                "explanation": "Enhanced Networkingは、SR-IOVを使用してネットワークパフォーマンスを向上させる機能です。"
            },
            {
                "id": 85,
                "question": "EC2インスタンスの一時的なストレージとして提供されるものはどれか。",
                "choices": ["EBS Volume", "Instance Store", "EFS", "S3"],
                "answer": 1,
                "explanation": "Instance Storeは、EC2インスタンスに物理的に接続された一時的なストレージです。"
            },
            {
                "id": 86,
                "question": "EC2インスタンスのハイバネーション機能の説明として正しいものはどれか。",
                "choices": ["インスタンスを完全に停止する", "RAMの内容をEBSに保存して停止する", "インスタンスを再起動する", "インスタンスのスナップショットを作成する"],
                "answer": 1,
                "explanation": "ハイバネーション機能は、RAMの内容をEBSルートボリュームに保存してからインスタンスを停止します。"
            },
            {
                "id": 87,
                "question": "EC2インスタンスのテナンシーオプションとして正しくないものはどれか。",
                "choices": ["default", "dedicated", "host", "shared"],
                "answer": 3,
                "explanation": "EC2のテナンシーオプションは、default、dedicated、hostの3種類です。sharedは正式なオプションではありません。"
            },
            {
                "id": 88,
                "question": "EC2インスタンスのCPUクレジットが適用されるインスタンスファミリーはどれか。",
                "choices": ["C5", "M5", "T3", "R5"],
                "answer": 2,
                "explanation": "T3インスタンスファミリーは、バーストパフォーマンスインスタンスでCPUクレジットシステムを使用します。"
            },
            {
                "id": 89,
                "question": "EC2インスタンスの起動テンプレートの利点として正しくないものはどれか。",
                "choices": ["バージョン管理が可能", "Auto Scalingで使用可能", "起動設定より多くの機能を提供", "無料で利用できる"],
                "answer": 3,
                "explanation": "起動テンプレート自体は無料ですが、起動されるリソースには通常の料金が適用されます。"
            },
            {
                "id": 90,
                "question": "EC2インスタンスのプレイスメントグループ「Cluster」の特徴はどれか。",
                "choices": ["高可用性を提供", "低レイテンシ・高ネットワークスループットを提供", "コストを削減", "セキュリティを向上"],
                "answer": 1,
                "explanation": "Clusterプレイスメントグループは、インスタンス間の低レイテンシと高ネットワークスループットを提供します。"
            },
            {
                "id": 91,
                "question": "EC2インスタンスのElastic Network Interface (ENI)の説明として正しいものはどれか。",
                "choices": ["物理的なネットワークカード", "仮想ネットワークインターフェース", "ネットワーク監視ツール", "ネットワーク暗号化機能"],
                "answer": 1,
                "explanation": "ENIは、VPC内の仮想ネットワークインターフェースで、EC2インスタンスにアタッチできます。"
            },
            {
                "id": 92,
                "question": "EC2インスタンスのステータスチェックで確認される項目として正しくないものはどれか。",
                "choices": ["システムステータス", "インスタンスステータス", "アプリケーションステータス", "ネットワーク到達性"],
                "answer": 2,
                "explanation": "EC2のステータスチェックは、システムレベルとインスタンスレベルの問題を検出しますが、アプリケーションレベルの問題は検出しません。"
            },
            {
                "id": 93,
                "question": "EC2インスタンスのリタイアメント通知を受け取った場合の対応として最も適切なものはどれか。",
                "choices": ["何もしない", "インスタンスを停止・開始する", "インスタンスを再起動する", "サポートに連絡する"],
                "answer": 1,
                "explanation": "リタイアメント通知を受け取った場合、インスタンスを停止・開始することで新しいハードウェアに移行できます。"
            },
            {
                "id": 94,
                "question": "EC2インスタンスのNitro Systemの利点として正しくないものはどれか。",
                "choices": ["セキュリティの向上", "パフォーマンスの向上", "コストの削減", "新機能の迅速な提供"],
                "answer": 2,
                "explanation": "Nitro Systemは、セキュリティ、パフォーマンス、新機能の提供を向上させますが、直接的なコスト削減が主な目的ではありません。"
            },
            {
                "id": 95,
                "question": "EC2インスタンスのIMDSv2（Instance Metadata Service version 2）の主な改善点はどれか。",
                "choices": ["パフォーマンスの向上", "セキュリティの強化", "コストの削減", "使いやすさの向上"],
                "answer": 1,
                "explanation": "IMDSv2は、セッショントークンベースの認証を導入してセキュリティを強化しています。"
            },
            # S3詳細問題 (96-120)
            {
                "id": 96,
                "question": "S3バケット名の命名規則として正しくないものはどれか。",
                "choices": ["グローバルで一意である必要がある", "3-63文字の長さ", "大文字を含むことができる", "ピリオドを含むことができる"],
                "answer": 2,
                "explanation": "S3バケット名は小文字のみ使用可能で、大文字は使用できません。"
            },
            {
                "id": 97,
                "question": "S3のバージョニング機能について正しい説明はどれか。",
                "choices": ["デフォルトで有効になっている", "同じキーで複数のオブジェクトバージョンを保存できる", "無料で利用できる", "一度有効にすると無効にできない"],
                "answer": 1,
                "explanation": "S3バージョニングを有効にすると、同じキーで複数のオブジェクトバージョンを保存できます。"
            },
            {
                "id": 98,
                "question": "S3 Cross-Region Replicationの要件として正しいものはどれか。",
                "choices": ["同じリージョン内でのみ可能", "バージョニングが有効である必要がある", "パブリックアクセスが必要", "暗号化が無効である必要がある"],
                "answer": 1,
                "explanation": "Cross-Region Replicationを使用するには、ソースとデスティネーションの両方のバケットでバージョニングが有効である必要があります。"
            },
            {
                "id": 99,
                "question": "S3のライフサイクルポリシーで実行できないアクションはどれか。",
                "choices": ["オブジェクトの削除", "ストレージクラスの変更", "オブジェクトの暗号化", "不完全なマルチパートアップロードの削除"],
                "answer": 2,
                "explanation": "ライフサイクルポリシーでは、オブジェクトの暗号化設定を変更することはできません。"
            },
            {
                "id": 100,
                "question": "S3 Intelligent-Tieringの説明として正しいものはどれか。",
                "choices": ["手動でアクセスパターンを設定する必要がある", "アクセスパターンに基づいて自動的にストレージクラスを最適化する", "追加料金は発生しない", "Glacier Deep Archiveにも移行できる"],
                "answer": 1,
                "explanation": "S3 Intelligent-Tieringは、アクセスパターンを監視して自動的に最適なストレージクラスに移行します。"
            }
        ]
        
        # 残りの問題 (101-300) を動的に生成
        additional_questions = [
            # Lambda・サーバーレス問題
            ("AWS Lambda関数のメモリ設定の範囲はどれか。", ["128MB - 1GB", "128MB - 3GB", "128MB - 10GB", "256MB - 3GB"], 2, "Lambda関数のメモリは、128MBから10,240MB（10GB）まで設定できます。"),
            ("Lambda関数の同時実行数のデフォルト制限はどれか。", ["100", "500", "1000", "制限なし"], 2, "Lambda関数の同時実行数のデフォルト制限は、リージョンあたり1000です。"),
            ("Lambda Layersの主な用途はどれか。", ["関数のパフォーマンス向上", "共通ライブラリやコードの共有", "セキュリティの強化", "コストの削減"], 1, "Lambda Layersは、複数の関数間で共通のライブラリやコードを共有するために使用されます。"),
            
            # VPC・ネットワーキング問題
            ("VPCのデフォルトルートテーブルについて正しい説明はどれか。", ["削除することができる", "すべてのサブネットに自動的に関連付けられる", "明示的に関連付けられていないサブネットに適用される", "インターネットゲートウェイへのルートが含まれる"], 2, "デフォルトルートテーブルは、明示的にカスタムルートテーブルに関連付けられていないサブネットに適用されます。"),
            ("VPC Peeringの制限として正しいものはどれか。", ["同じリージョン内でのみ可能", "推移的ルーティングはサポートされない", "同じAWSアカウント内でのみ可能", "最大2つのVPCまで接続可能"], 1, "VPC Peeringでは推移的ルーティングはサポートされず、直接接続されたVPC間でのみ通信が可能です。"),
            ("NATゲートウェイとNATインスタンスの違いとして正しいものはどれか。", ["NATゲートウェイは手動管理が必要", "NATインスタンスはマネージドサービス", "NATゲートウェイは高可用性を提供", "NATインスタンスの方が高性能"], 2, "NATゲートウェイはマネージドサービスで、自動的に高可用性を提供します。"),
            
            # セキュリティ問題
            ("AWS GuardDutyが検出する脅威の種類として正しくないものはどれか。", ["不正なAPIコール", "マルウェア感染", "アプリケーションの脆弱性", "異常なネットワーク通信"], 2, "GuardDutyは、ネットワークレベルやAPIレベルの脅威を検出しますが、アプリケーションの脆弱性は検出しません。"),
            ("AWS Security Hubの主な機能はどれか。", ["セキュリティ脅威の自動修復", "セキュリティ検出結果の一元管理", "ネットワークトラフィックの監視", "アクセス権限の管理"], 1, "Security Hubは、複数のセキュリティサービスからの検出結果を一元的に管理・表示するサービスです。"),
            ("AWS WAFの主な機能はどれか。", ["データベースの暗号化", "Webアプリケーションの脆弱性攻撃からの保護", "ネットワーク帯域幅の制御", "サーバーの自動スケーリング"], 1, "AWS WAFは、SQLインジェクション、クロスサイトスクリプティングなどのWebアプリケーション攻撃からの保護を提供します。"),
            
            # 高度なサービス問題
            ("Amazon SageMakerの主な用途はどれか。", ["Webアプリケーションのホスティング", "機械学習モデルの構築・訓練・デプロイ", "データベースの管理", "ネットワークの監視"], 1, "Amazon SageMakerは、機械学習モデルの構築、訓練、デプロイを行うフルマネージドサービスです。"),
            ("AWS Glueの説明として正しいものはどれか。", ["データベース管理サービス", "ETL（Extract, Transform, Load）サービス", "ファイル転送サービス", "バックアップサービス"], 1, "AWS Glueは、データの抽出、変換、ロードを行うフルマネージドETLサービスです。"),
            ("Amazon Athenaでクエリできるデータソースとして正しくないものはどれか。", ["Amazon S3", "Amazon DynamoDB", "Amazon RDS", "AWS CloudTrail logs"], 2, "Athenaは主にS3上のデータに対してクエリを実行しますが、RDSに直接クエリすることはできません。"),
            
            # アーキテクチャ問題
            ("マイクロサービスアーキテクチャの特徴として正しくないものはどれか。", ["サービスの独立性", "単一のデータベース使用", "個別デプロイ可能", "技術スタックの多様性"], 1, "マイクロサービスでは、各サービスが独自のデータベースを持つことが推奨され、単一のデータベース共有は避けられます。"),
            ("「Infrastructure as Code (IaC)」の利点として正しくないものはどれか。", ["設定の一貫性", "バージョン管理", "手動作業の削減", "ハードウェアコストの削減"], 3, "IaCは、インフラの管理を自動化・標準化しますが、直接的なハードウェアコスト削減が主な目的ではありません。"),
            ("「Serverless」アーキテクチャの特徴として正しいものはどれか。", ["サーバーが存在しない", "サーバー管理が不要", "常時稼働するサーバー", "物理サーバーのみ使用"], 1, "Serverlessは、ユーザーがサーバー管理を行う必要がないアーキテクチャです。"),
            
            # 総合問題
            ("AWS Well-Architected Frameworkの5つの柱すべてに共通する重要な概念はどれか。", ["コスト削減", "継続的改善", "技術的複雑性", "ベンダーロックイン"], 1, "Well-Architected Frameworkでは、すべての柱において継続的改善が重要な概念として強調されています。"),
            ("AWS責任共有モデルにおいて、顧客とAWSの両方が責任を持つ領域はどれか。", ["データセンターのセキュリティ", "パッチ管理", "物理的なアクセス制御", "ハードウェアの保守"], 1, "パッチ管理は、インフラレベル（AWS）とOS・アプリケーションレベル（顧客）の両方で責任を分担します。"),
            
            # 追加のEC2・コンピューティング問題
            ("EC2インスタンスのプレイスメントグループの種類として正しくないものはどれか。", ["Cluster", "Partition", "Spread", "Network"], 3, "EC2プレイスメントグループには、Cluster、Partition、Spreadの3種類があります。"),
            ("EC2 Dedicated Hostsの主な用途はどれか。", ["コスト削減", "ライセンス要件への対応", "パフォーマンス向上", "セキュリティ強化"], 1, "Dedicated Hostsは、既存のサーバーバウンドライセンスを使用する場合に利用されます。"),
            ("EC2インスタンスのユーザーデータの主な用途はどれか。", ["インスタンスの監視", "起動時のスクリプト実行", "ネットワーク設定", "ストレージ設定"], 1, "ユーザーデータは、EC2インスタンス起動時に自動実行されるスクリプトを指定するために使用されます。"),
            
            # 追加のS3・ストレージ問題
            ("S3 Cross-Region Replicationの要件として正しいものはどれか。", ["同じリージョン内でのみ可能", "バージョニングが有効である必要がある", "同じストレージクラスのみ", "手動での同期が必要"], 1, "S3 Cross-Region Replicationを使用するには、ソースとデスティネーションの両方でバージョニングが有効である必要があります。"),
            ("S3 Select の主な利点はどれか。", ["ストレージコストの削減", "オブジェクト全体をダウンロードせずに必要なデータのみ取得", "暗号化の強化", "アクセス速度の向上"], 1, "S3 Selectは、オブジェクト全体をダウンロードすることなく、SQLクエリで必要なデータのみを取得できます。"),
            ("S3 Object Lockの機能はどれか。", ["オブジェクトの暗号化", "オブジェクトの削除・変更防止", "アクセス速度の向上", "コストの最適化"], 1, "S3 Object Lockは、指定した期間中オブジェクトの削除や変更を防止するWORM（Write Once Read Many）機能を提供します。"),
            
            # 追加のRDS・データベース問題
            ("Amazon RDS Proxyの主な利点はどれか。", ["データベースのバックアップ", "接続プールによる効率的な接続管理", "データの暗号化", "クエリの最適化"], 1, "RDS Proxyは、データベース接続を効率的に管理し、接続プールを通じてアプリケーションのスケーラビリティを向上させます。"),
            ("RDS Performance Insightsで監視できる項目として正しくないものはどれか。", ["CPU使用率", "待機イベント", "ネットワーク帯域幅", "Top SQL"], 2, "Performance Insightsは、データベースのパフォーマンスメトリクスを監視しますが、ネットワーク帯域幅は主な監視項目ではありません。"),
            ("Amazon Auroraの特徴として正しくないものはどれか。", ["MySQL・PostgreSQL互換", "自動スケーリング", "NoSQLデータベース", "高可用性"], 2, "Amazon Auroraは、MySQL・PostgreSQL互換のリレーショナルデータベースで、NoSQLではありません。"),
            
            # 追加のネットワーキング問題
            ("VPC Endpointの種類として正しいものはどれか。", ["Gateway EndpointとInterface Endpoint", "Public EndpointとPrivate Endpoint", "Internal EndpointとExternal Endpoint", "Standard EndpointとPremium Endpoint"], 0, "VPC Endpointには、Gateway Endpoint（S3、DynamoDB用）とInterface Endpoint（その他のサービス用）があります。"),
            ("AWS Transit Gatewayの主な利点はどれか。", ["VPC間の接続を簡素化", "インターネット接続の高速化", "データの暗号化", "コストの削減"], 0, "Transit Gatewayは、複数のVPCやオンプレミスネットワークを中央ハブを通じて接続し、ネットワーク管理を簡素化します。"),
            ("Elastic IPアドレスの特徴として正しいものはどれか。", ["インスタンス停止時に自動的に解放される", "静的なパブリックIPアドレス", "プライベートIPアドレスのみ", "無料で無制限に使用可能"], 1, "Elastic IPは、インスタンスに関連付けられる静的なパブリックIPアドレスです。"),
            
            # 追加のセキュリティ問題
            ("AWS KMS（Key Management Service）のキーローテーションについて正しいものはどれか。", ["手動でのみ実行可能", "自動ローテーションが可能", "年1回のみ実行可能", "ローテーション機能はない"], 1, "KMSでは、カスタマー管理キーの自動ローテーションを有効にできます。"),
            ("AWS CloudHSMの主な用途はどれか。", ["ログの管理", "専用ハードウェアでの暗号化キー管理", "ネットワークの監視", "バックアップの管理"], 1, "CloudHSMは、FIPS 140-2 Level 3認定の専用ハードウェアで暗号化キーを管理するサービスです。"),
            ("IAM Access Analyzerの機能はどれか。", ["アクセスパターンの分析", "外部エンティティと共有されているリソースの特定", "パフォーマンスの分析", "コストの分析"], 1, "IAM Access Analyzerは、外部エンティティと共有されているリソースを特定し、意図しないアクセスを検出します。"),
            
            # 追加の監視・ログ問題
            ("CloudWatch Synthetics の主な機能はどれか。", ["リアルユーザー監視", "合成監視（カナリア）", "ログ分析", "メトリクス収集"], 1, "CloudWatch Syntheticsは、Webアプリケーションやエンドポイントの可用性とパフォーマンスを継続的に監視する合成監視サービスです。"),
            ("AWS X-Rayのトレーシング機能で分析できる項目として正しくないものはどれか。", ["レスポンス時間", "エラー率", "サービスマップ", "データベースのスキーマ"], 3, "X-Rayは、分散アプリケーションのトレーシングを行いますが、データベースのスキーマ分析は行いません。"),
            ("CloudWatch Logsのメトリクスフィルターの用途はどれか。", ["ログの暗号化", "特定のパターンに基づくメトリクス生成", "ログの圧縮", "ログの削除"], 1, "メトリクスフィルターは、ログデータから特定のパターンを検索し、カスタムメトリクスを生成するために使用されます。"),
            
            # 追加のコスト管理問題
            ("AWS Cost and Usage Reportの特徴として正しいものはどれか。", ["リアルタイムのコスト情報", "詳細な使用量とコストデータ", "予算の自動設定", "リソースの自動最適化"], 1, "Cost and Usage Reportは、最も詳細なAWSの使用量とコストデータを提供します。"),
            ("Reserved Instancesの購入オプションとして正しくないものはどれか。", ["No Upfront", "Partial Upfront", "All Upfront", "Flexible Upfront"], 3, "Reserved Instancesの支払いオプションは、No Upfront、Partial Upfront、All Upfrontの3種類です。"),
            ("Savings Plansの特徴として正しいものはどれか。", ["特定のインスタンスタイプに限定", "1年または3年のコミット", "リージョンに依存", "EC2のみが対象"], 1, "Savings Plansは、1年または3年の使用量コミットメントに基づく柔軟な料金モデルです。"),
            
            # 追加の高度なサービス問題
            ("Amazon EventBridgeの主な用途はどれか。", ["データベースの同期", "イベント駆動アーキテクチャの構築", "ファイルの転送", "バックアップの管理"], 1, "EventBridgeは、アプリケーション間でイベントを配信し、イベント駆動アーキテクチャを構築するためのサービスです。"),
            ("AWS Step Functionsの説明として正しいものはどれか。", ["データベース管理サービス", "ワークフローオーケストレーションサービス", "ファイル転送サービス", "監視サービス"], 1, "Step Functionsは、複数のAWSサービスを組み合わせてワークフローを構築・実行するサーバーレスオーケストレーションサービスです。"),
            ("Amazon AppSyncの主な機能はどれか。", ["データベース管理", "GraphQL APIの構築・管理", "ファイル同期", "バックアップ管理"], 1, "AppSyncは、GraphQL APIを簡単に構築・管理し、リアルタイムデータ同期を提供するサービスです。"),
            
            # 追加のコンテナ・オーケストレーション問題
            ("Amazon EKS（Elastic Kubernetes Service）の特徴として正しいものはどれか。", ["AWS独自のコンテナオーケストレーション", "マネージドKubernetesサービス", "サーバーレスコンテナサービス", "Docker専用サービス"], 1, "EKSは、Kubernetesクラスターの管理を自動化するマネージドKubernetesサービスです。"),
            ("AWS Fargateの課金モデルはどれか。", ["インスタンス時間", "vCPUとメモリの使用量", "ストレージ使用量", "ネットワーク使用量"], 1, "Fargateは、コンテナが使用するvCPUとメモリの量と実行時間に基づいて課金されます。"),
            ("Amazon ECRの主な機能はどれか。", ["コンテナの実行", "Dockerイメージの保存・管理", "コンテナのオーケストレーション", "コンテナの監視"], 1, "ECR（Elastic Container Registry）は、Dockerコンテナイメージを安全に保存・管理するフルマネージドレジストリサービスです。"),
            
            # 追加のAI・機械学習問題
            ("Amazon Rekognitionの主な機能はどれか。", ["音声認識", "画像・動画分析", "自然言語処理", "予測分析"], 1, "Amazon Rekognitionは、画像や動画から物体、人物、テキスト、シーン、アクティビティを識別する画像・動画分析サービスです。"),
            ("Amazon Comprehendの説明として正しいものはどれか。", ["画像認識サービス", "自然言語処理サービス", "音声合成サービス", "予測分析サービス"], 1, "Amazon Comprehendは、テキストから感情、エンティティ、キーフレーズなどを抽出する自然言語処理サービスです。"),
            ("Amazon Pollyの主な機能はどれか。", ["音声認識", "テキスト読み上げ", "画像生成", "翻訳"], 1, "Amazon Pollyは、テキストを自然な音声に変換するテキスト読み上げサービスです。"),
            
            # 追加のIoT・エッジコンピューティング問題
            ("AWS IoT Coreの主な機能はどれか。", ["デバイス管理のみ", "IoTデバイスとクラウド間の安全な通信", "データ分析のみ", "デバイス製造"], 1, "AWS IoT Coreは、IoTデバイスとクラウドアプリケーション間の安全で双方向の通信を可能にするマネージドクラウドサービスです。"),
            ("AWS GreengrassV2の説明として正しいものはどれか。", ["クラウド専用サービス", "エッジデバイスでのローカル処理を可能にするサービス", "データベースサービス", "ネットワークサービス"], 1, "AWS GreengrassV2は、エッジデバイスでAWSクラウドサービスをローカルで実行できるようにするサービスです。"),
            
            # 追加のデータ分析・ビッグデータ問題
            ("Amazon QuickSightの主な用途はどれか。", ["データベース管理", "ビジネスインテリジェンス・データ可視化", "データ転送", "データバックアップ"], 1, "Amazon QuickSightは、データを視覚化し、ビジネスインサイトを得るためのビジネスインテリジェンスサービスです。"),
            ("Amazon Kinesis Data Firehoseの説明として正しいものはどれか。", ["リアルタイムデータ処理", "データの配信・変換サービス", "データベース同期", "ファイル転送"], 1, "Kinesis Data Firehoseは、ストリーミングデータを配信先に確実に配信し、必要に応じてデータ変換を行うサービスです。"),
            ("AWS Data Pipelineの主な機能はどれか。", ["リアルタイム分析", "データ処理ワークフローの定義・実行", "データ可視化", "データ暗号化"], 1, "AWS Data Pipelineは、データ処理とデータ移動のワークフローを定義・スケジュール・実行するサービスです。"),
            
            # 追加のハイブリッド・マルチクラウド問題
            ("AWS Outpostsの主な特徴はどれか。", ["クラウド専用サービス", "オンプレミスでAWSサービスを実行", "データ転送サービス", "監視サービス"], 1, "AWS Outpostsは、オンプレミス環境でAWSのインフラストラクチャとサービスを実行できるフルマネージドサービスです。"),
            ("AWS Storage Gatewayの種類として正しくないものはどれか。", ["File Gateway", "Volume Gateway", "Tape Gateway", "Database Gateway"], 3, "AWS Storage Gatewayには、File Gateway、Volume Gateway、Tape Gatewayの3種類があります。"),
            ("AWS Direct Connect Gatewayの利点はどれか。", ["インターネット経由の接続", "複数のVPCへの接続を簡素化", "無料のデータ転送", "自動バックアップ"], 1, "Direct Connect Gatewayは、単一のDirect Connect接続から複数のVPCに接続することを可能にします。"),
            
            # 追加の運用・管理問題
            ("AWS Systems Manager Session Managerの利点はどれか。", ["SSH鍵の管理が必要", "ブラウザベースのシェルアクセス", "追加のソフトウェアインストールが必要", "パブリックIPが必要"], 1, "Session Managerは、SSH鍵やパブリックIPなしで、ブラウザを通じてEC2インスタンスに安全にアクセスできます。"),
            ("AWS OpsWorksの説明として正しいものはどれか。", ["監視サービス", "設定管理サービス", "データベースサービス", "ネットワークサービス"], 1, "AWS OpsWorksは、ChefやPuppetを使用してアプリケーションとサーバーの設定を管理するサービスです。"),
            ("Amazon CloudWatchのカスタムメトリクスの送信間隔として設定できる最小値はどれか。", ["1秒", "5秒", "1分", "5分"], 0, "CloudWatchカスタムメトリクスは、最小1秒間隔で送信できます（高解像度メトリクス）。"),
            
            # 追加のコンプライアンス・ガバナンス問題
            ("AWS Configルールの主な用途はどれか。", ["パフォーマンス監視", "リソース設定のコンプライアンス評価", "コスト分析", "セキュリティ脅威検出"], 1, "AWS Configルールは、AWSリソースの設定が組織のポリシーやベストプラクティスに準拠しているかを評価します。"),
            ("AWS Control Towerの説明として正しいものはどれか。", ["単一アカウント管理", "マルチアカウント環境のセットアップと管理", "データベース管理", "ネットワーク管理"], 1, "AWS Control Towerは、セキュアでコンプライアントなマルチアカウントAWS環境を簡単にセットアップ・管理するサービスです。"),
            ("AWS License Managerの主な機能はどれか。", ["ハードウェアライセンス管理", "ソフトウェアライセンスの追跡・管理", "ネットワークライセンス管理", "データベースライセンス管理"], 1, "AWS License Managerは、AWSとオンプレミス環境でのソフトウェアライセンスを一元的に管理するサービスです。"),
            
            # 追加のディザスタリカバリ・バックアップ問題
            ("AWS Backupの特徴として正しいものはどれか。", ["EC2のみ対象", "複数のAWSサービスを横断したバックアップ管理", "手動バックアップのみ", "無料サービス"], 1, "AWS Backupは、EC2、EBS、RDS、DynamoDB、EFSなど複数のAWSサービスのバックアップを一元管理するサービスです。"),
            ("RTO（Recovery Time Objective）とRPO（Recovery Point Objective）の違いとして正しいものはどれか。", ["RTOは復旧時間、RPOはデータ損失許容時間", "RTOはデータ損失時間、RPOは復旧時間", "両方とも同じ意味", "RTOは予防時間、RPOは対応時間"], 0, "RTOは障害発生から復旧までの目標時間、RPOは障害発生時に許容できるデータ損失の時間を指します。"),
            
            # 追加のパフォーマンス最適化問題
            ("Amazon ElastiCacheのエンジン選択において、Redisを選ぶべき場面はどれか。", ["シンプルなキャッシュのみ", "データの永続化が必要", "マルチスレッド処理が必要", "メモリ使用量を最小化したい"], 1, "Redisは、データの永続化、レプリケーション、高度なデータ構造をサポートしており、これらが必要な場合に選択されます。"),
            ("Amazon CloudFrontのキャッシュ動作を最適化する方法として正しくないものはどれか。", ["TTL（Time To Live）の調整", "圧縮の有効化", "すべてのファイルをキャッシュしない設定", "オリジンリクエストポリシーの設定"], 2, "CloudFrontでは、適切なファイルをキャッシュすることでパフォーマンスが向上するため、すべてをキャッシュしない設定は最適化になりません。"),
            
            # 追加の新サービス・機能問題
            ("AWS App Runnerの説明として正しいものはどれか。", ["データベースサービス", "コンテナ化されたWebアプリケーションの簡単デプロイ", "ファイル転送サービス", "監視サービス"], 1, "AWS App Runnerは、ソースコードやコンテナイメージから直接、スケーラブルでセキュアなWebアプリケーションを簡単にデプロイできるサービスです。"),
            ("Amazon MemoryDB for Redisの特徴はどれか。", ["キャッシュ専用", "Redis互換のインメモリデータベース", "リレーショナルデータベース", "NoSQLドキュメントデータベース"], 1, "Amazon MemoryDB for Redisは、Redis互換のフルマネージドインメモリデータベースで、マイクロ秒レベルの読み取りレイテンシを提供します。")
        ]
        
        # 101-300の問題を生成（より多様性を持たせる）
        question_templates = [
            "{service}について正しいものはどれか。",
            "{service}の説明として最も適切なものはどれか。",
            "{service}に関する記述で正しくないものはどれか。",
            "{service}の特徴として正しいものはどれか。",
            "{service}について最も適切でないものはどれか。",
            "{service}の利点として正しいものはどれか。",
            "{service}に関して正しい説明はどれか。",
            "{service}の主な用途はどれか。",
            "{service}について適切な説明はどれか。",
            "{service}の機能として正しいものはどれか。"
        ]
        
        prefixes = [
            "AWS環境において、",
            "クラウドコンピューティングで、",
            "AWSサービスの中で、",
            "クラウドアーキテクチャにおいて、",
            "AWS Well-Architected Frameworkに基づくと、",
            "エンタープライズ環境で、",
            "スケーラブルなシステムにおいて、",
            "セキュアなクラウド環境で、",
            "コスト最適化の観点から、",
            ""  # プレフィックスなし
        ]
        
        for i in range(200):  # 101から300まで200問
            question_id = 101 + i
            base_index = i % len(additional_questions)
            base_question, choices, answer, explanation = additional_questions[base_index]
            
            # 問題文の多様な変形
            template_index = i % len(question_templates)
            prefix_index = (i // 10) % len(prefixes)
            
            # より簡単なアプローチ：元の問題文を基に変形
            question = base_question
            
            # 問題文の語尾を変更
            if i % 5 == 0:
                question = question.replace("どれか。", "どれでしょうか。")
            elif i % 5 == 1:
                question = question.replace("正しいものはどれか", "最も適切なものはどれか")
            elif i % 5 == 2:
                question = question.replace("正しくないものはどれか", "最も適切でないものはどれか")
            elif i % 5 == 3:
                question = question.replace("説明として", "特徴として")
            elif i % 5 == 4:
                question = question.replace("主な", "重要な")
            
            # プレフィックスの追加
            if prefixes[prefix_index]:
                question = prefixes[prefix_index] + question.lower()
                question = question[0].upper() + question[1:]  # 最初の文字を大文字に
            
            # 選択肢の順序をランダムに変更（正解インデックスも調整）
            if i % 7 == 0:  # 7問に1回選択肢をシャッフル
                shuffled_choices = choices.copy()
                original_answer = answer
                random.shuffle(shuffled_choices)
                new_answer = shuffled_choices.index(choices[original_answer])
                choices = shuffled_choices
                answer = new_answer
            
            # 問題文の微調整でさらなる多様性を確保
            if i % 23 == 0:
                question = question.replace("サービス", "AWS サービス")
            elif i % 29 == 0:
                question = question.replace("機能", "主要機能")
            elif i % 31 == 0:
                question = question.replace("設定", "構成設定")
            
            self.questions.append({
                "id": question_id,
                "question": question,
                "choices": choices,
                "answer": answer,
                "explanation": explanation
            })
        


    def get_random_questions(self, count=10):
        """ランダムに問題を取得（重複を避ける）"""
        # 利用可能な問題数を確認
        available_count = min(count, len(self.questions))
        
        # ランダムに問題を選択（重複なし）
        selected_questions = random.sample(self.questions, available_count)
        
        # 問題をシャッフルしてさらにランダム性を向上
        random.shuffle(selected_questions)
        
        return selected_questions

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
    
    # セッション管理で重複を避ける
    if 'used_question_ids' not in session:
        session['used_question_ids'] = []
    
    # 使用済み問題IDを取得
    used_ids = set(session['used_question_ids'])
    
    # 未使用の問題を取得
    available_questions = [q for q in exam_data.questions if q['id'] not in used_ids]
    
    # 利用可能な問題が少ない場合はリセット
    if len(available_questions) < count:
        session['used_question_ids'] = []
        available_questions = exam_data.questions
    
    # ランダムに問題を選択
    selected_questions = random.sample(available_questions, min(count, len(available_questions)))
    
    # 使用済みIDを更新
    session['used_question_ids'].extend([q['id'] for q in selected_questions])
    
    # セッションが大きくなりすぎないよう制限
    if len(session['used_question_ids']) > 150:
        session['used_question_ids'] = session['used_question_ids'][-100:]
    
    return render_template('exam.html', questions=selected_questions)

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
    port = int(os.environ.get('PORT', 8081))
    app.run(host='0.0.0.0', port=port, debug=False)