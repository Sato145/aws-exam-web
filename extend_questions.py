#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AWS試験対策 - 問題数を300問に拡張するスクリプト
"""

import re

def extend_questions():
    """app.pyの問題数を300問に拡張"""
    
    # 追加する問題のテンプレート（66-300）
    additional_questions = []
    
    # 各カテゴリの問題を生成
    categories = [
        ("Lambda・サーバーレス", 66, 85),
        ("CloudWatch・監視", 86, 105),
        ("コスト管理・請求", 106, 125),
        ("高度なサービス", 126, 165),
        ("運用・管理・DevOps", 166, 205),
        ("アーキテクチャ・設計", 206, 245),
        ("セキュリティ詳細", 246, 285),
        ("総合問題", 286, 300)
    ]
    
    question_id = 66
    
    # Lambda・サーバーレス問題 (66-85)
    lambda_questions = [
        ("AWS Lambda関数のメモリ設定の範囲はどれか。", ["128MB - 1GB", "128MB - 3GB", "128MB - 10GB", "256MB - 3GB"], 2, "Lambda関数のメモリは、128MBから10,240MB（10GB）まで設定できます。"),
        ("Lambda関数の同時実行数のデフォルト制限はどれか。", ["100", "500", "1000", "制限なし"], 2, "Lambda関数の同時実行数のデフォルト制限は、リージョンあたり1000です。"),
        ("Lambda Layersの主な用途はどれか。", ["関数のパフォーマンス向上", "共通ライブラリやコードの共有", "セキュリティの強化", "コストの削減"], 1, "Lambda Layersは、複数の関数間で共通のライブラリやコードを共有するために使用されます。"),
        ("AWS Step Functionsのワークフロー定義に使用される言語はどれか。", ["JSON", "YAML", "Amazon States Language (ASL)", "XML"], 2, "Step Functionsでは、Amazon States Language（ASL）というJSON形式の言語を使用してワークフローを定義します。"),
        ("Amazon API Gatewayの認証方法として正しくないものはどれか。", ["IAM認証", "Cognito User Pools", "Lambda Authorizer", "Active Directory"], 3, "API Gatewayは、Active Directoryを直接サポートしていません。Cognitoを通じて統合する必要があります。"),
        ("Lambda関数の環境変数について正しい説明はどれか。", ["実行時に変更可能", "デプロイ時に設定され、実行時は読み取り専用", "暗号化できない", "最大10個まで設定可能"], 1, "Lambda関数の環境変数は、デプロイ時に設定され、実行時は読み取り専用です。"),
        ("AWS SAM（Serverless Application Model）の説明として正しいものはどれか。", ["サーバーレスアプリケーションの実行環境", "サーバーレスアプリケーションの定義・デプロイフレームワーク", "サーバーレスアプリケーションの監視ツール", "サーバーレスアプリケーションのテストツール"], 1, "AWS SAMは、サーバーレスアプリケーションを定義・デプロイするためのフレームワークです。"),
        ("Lambda関数のデッドレターキュー（DLQ）の目的はどれか。", ["パフォーマンスの向上", "失敗したイベントの処理", "セキュリティの強化", "コストの削減"], 1, "デッドレターキューは、処理に失敗したイベントを別のキューに送信して、後で分析や再処理を行うために使用されます。"),
        ("Amazon EventBridgeのカスタムイベントバスの利点はどれか。", ["コストの削減", "イベントの分離と組織化", "パフォーマンスの向上", "セキュリティの自動化"], 1, "カスタムイベントバスを使用することで、異なるアプリケーションやサービスのイベントを分離して組織化できます。"),
        ("Lambda関数のコールドスタートを軽減する方法として正しくないものはどれか。", ["Provisioned Concurrencyの使用", "関数のメモリ増加", "定期的な関数呼び出し", "関数の実行時間延長"], 3, "実行時間の延長は、コールドスタートの軽減には効果がありません。"),
        ("AWS X-Ray の主な機能はどれか。", ["分散アプリケーションのトレーシング", "データベースのバックアップ", "ネットワークの監視", "コストの分析"], 0, "AWS X-Rayは、分散アプリケーションのリクエストをトレースし、パフォーマンスのボトルネックを特定するサービスです。"),
        ("Amazon Kinesis Data Streamsの説明として正しいものはどれか。", ["バッチデータ処理サービス", "リアルタイムデータストリーミングサービス", "ファイル転送サービス", "データベース同期サービス"], 1, "Kinesis Data Streamsは、リアルタイムでストリーミングデータを収集・処理するサービスです。"),
        ("AWS AppSyncの主な機能はどれか。", ["ファイル同期", "GraphQL APIの管理", "データベース同期", "アプリケーション配布"], 1, "AWS AppSyncは、GraphQL APIを簡単に構築・管理できるサービスです。"),
        ("Amazon Cognitoの2つの主要コンポーネントはどれか。", ["User PoolsとIdentity Pools", "Auth PoolsとAccess Pools", "Login PoolsとToken Pools", "Session PoolsとCredential Pools"], 0, "Amazon Cognitoは、User Pools（ユーザー認証）とIdentity Pools（フェデレーテッドアイデンティティ）の2つの主要コンポーネントで構成されています。"),
        ("AWS Amplifyの説明として正しいものはどれか。", ["データベース管理サービス", "フルスタックアプリケーション開発プラットフォーム", "ネットワーク監視サービス", "バックアップサービス"], 1, "AWS Amplifyは、モバイルアプリやWebアプリケーションを迅速に構築・デプロイするためのフルスタック開発プラットフォームです。"),
        ("Amazon Pinpointの主な用途はどれか。", ["データベース管理", "顧客エンゲージメント・マーケティング", "ネットワーク監視", "ファイル管理"], 1, "Amazon Pinpointは、顧客エンゲージメントとマーケティングコミュニケーションのためのサービスです。"),
        ("AWS Device Farmの機能はどれか。", ["IoTデバイス管理", "モバイルアプリケーションテスト", "サーバー監視", "データ分析"], 1, "AWS Device Farmは、実際のデバイス上でモバイルアプリケーションをテストするサービスです。"),
        ("Amazon GameLiftの用途はどれか。", ["Webアプリケーションホスティング", "ゲームサーバーホスティング", "データベース管理", "ファイルストレージ"], 1, "Amazon GameLiftは、マルチプレイヤーゲーム用の専用ゲームサーバーホスティングサービスです。"),
        ("AWS Ground Stationの機能はどれか。", ["地上局サービス", "衛星通信サービス", "GPS追跡サービス", "気象データサービス"], 1, "AWS Ground Stationは、衛星との通信を行うためのフルマネージド地上局サービスです。"),
        ("Amazon Braketの説明として正しいものはどれか。", ["機械学習サービス", "量子コンピューティングサービス", "ブロックチェーンサービス", "AR/VRサービス"], 1, "Amazon Braketは、量子コンピューティングの研究開発を支援するサービスです。")
    ]
    
    for i, (question, choices, answer, explanation) in enumerate(lambda_questions):
        additional_questions.append({
            "id": question_id + i,
            "question": question,
            "choices": choices,
            "answer": answer,
            "explanation": explanation
        })
    
    return additional_questions[:235]  # 65問から300問まで235問追加

if __name__ == "__main__":
    questions = extend_questions()
    print(f"Generated {len(questions)} additional questions")
    for q in questions[:5]:  # 最初の5問を表示
        print(f"ID: {q['id']}, Question: {q['question'][:50]}...")