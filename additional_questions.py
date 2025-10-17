#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AWS試験対策 - 追加問題データ (61-300)
"""

additional_questions = [
    # EC2 詳細問題 (61-80)
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
        "question": "EC2インスタンスの配置グループ（Placement Group）の種類として正しくないものはどれか。",
        "choices": [
            "Cluster",
            "Partition",
            "Spread",
            "Network"
        ],
        "answer": 3,
        "explanation": "EC2の配置グループには、Cluster、Partition、Spreadの3種類があります。Networkは配置グループの種類ではありません。"
    },
    {
        "id": 63,
        "question": "EC2 Dedicated Hostsの主な利点はどれか。",
        "choices": [
            "コストの削減",
            "パフォーマンスの向上",
            "ライセンス要件への対応",
            "自動スケーリング"
        ],
        "answer": 2,
        "explanation": "Dedicated Hostsは、既存のサーバーバウンドソフトウェアライセンスを使用する際のライセンス要件に対応するために使用されます。"
    },
    {
        "id": 64,
        "question": "EC2インスタンスの起動時に実行されるスクリプトを指定する機能はどれか。",
        "choices": [
            "User Data",
            "Instance Metadata",
            "Security Groups",
            "Key Pairs"
        ],
        "answer": 0,
        "explanation": "User Dataを使用して、EC2インスタンスの起動時に実行されるスクリプトを指定できます。"
    },
    {
        "id": 65,
        "question": "EC2インスタンスの状態で、課金が停止されるものはどれか。",
        "choices": [
            "Running",
            "Stopped",
            "Stopping",
            "Pending"
        ],
        "answer": 1,
        "explanation": "EC2インスタンスがStopped状態の場合、コンピューティング料金の課金は停止されます（ストレージ料金は継続）。"
    },
    {
        "id": 66,
        "question": "EC2インスタンスタイプで、機械学習ワークロードに最適化されたファミリーはどれか。",
        "choices": [
            "C5",
            "R5",
            "P3",
            "I3"
        ],
        "answer": 2,
        "explanation": "P3インスタンスファミリーは、機械学習とHPCワークロード用にGPUを搭載した最適化されたインスタンスです。"
    },
    {
        "id": 67,
        "question": "EC2 Spot Instancesの価格決定方式はどれか。",
        "choices": [
            "固定価格",
            "需要と供給による変動価格",
            "時間単位の固定価格",
            "使用量に応じた従量課金"
        ],
        "answer": 1,
        "explanation": "Spot Instancesの価格は、需要と供給に基づいて変動し、通常のオンデマンド価格より大幅に安くなります。"
    },
    {
        "id": 68,
        "question": "EC2インスタンスの監視で、デフォルトで有効になっているメトリクスの間隔はどれか。",
        "choices": [
            "1分間隔",
            "5分間隔",
            "10分間隔",
            "15分間隔"
        ],
        "answer": 1,
        "explanation": "EC2インスタンスの基本監視では、デフォルトで5分間隔でメトリクスが収集されます。"
    },
    {
        "id": 69,
        "question": "EC2インスタンスのネットワークパフォーマンスを向上させる機能はどれか。",
        "choices": [
            "Enhanced Networking",
            "Elastic IP",
            "Security Groups",
            "Instance Store"
        ],
        "answer": 0,
        "explanation": "Enhanced Networkingは、SR-IOVを使用してネットワークパフォーマンスを向上させる機能です。"
    },
    {
        "id": 70,
        "question": "EC2インスタンスの一時的なストレージとして提供されるものはどれか。",
        "choices": [
            "EBS Volume",
            "Instance Store",
            "EFS",
            "S3"
        ],
        "answer": 1,
        "explanation": "Instance Storeは、EC2インスタンスに物理的に接続された一時的なストレージです。"
    },
    
    # S3 詳細問題 (71-90)
    {
        "id": 71,
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
        "id": 72,
        "question": "S3のバージョニング機能について正しい説明はどれか。",
        "choices": [
            "デフォルトで有効になっている",
            "同じキーで複数のオブジェクトバージョンを保存できる",
            "無料で利用できる",
            "一度有効にすると無効にできない"
        ],
        "answer": 1,
        "explanation": "S3バージョニングを有効にすると、同じキーで複数のオブジェクトバージョンを保存できます。"
    },
    {
        "id": 73,
        "question": "S3 Cross-Region Replicationの要件として正しいものはどれか。",
        "choices": [
            "同じリージョン内でのみ可能",
            "バージョニングが有効である必要がある",
            "パブリックアクセスが必要",
            "暗号化が無効である必要がある"
        ],
        "answer": 1,
        "explanation": "Cross-Region Replicationを使用するには、ソースとデスティネーションの両方のバケットでバージョニングが有効である必要があります。"
    },
    {
        "id": 74,
        "question": "S3のライフサイクルポリシーで実行できないアクションはどれか。",
        "choices": [
            "オブジェクトの削除",
            "ストレージクラスの変更",
            "オブジェクトの暗号化",
            "不完全なマルチパートアップロードの削除"
        ],
        "answer": 2,
        "explanation": "ライフサイクルポリシーでは、オブジェクトの暗号化設定を変更することはできません。"
    },
    {
        "id": 75,
        "question": "S3 Intelligent-Tieringの説明として正しいものはどれか。",
        "choices": [
            "手動でアクセスパターンを設定する必要がある",
            "アクセスパターンに基づいて自動的にストレージクラスを最適化する",
            "追加料金は発生しない",
            "Glacier Deep Archiveにも移行できる"
        ],
        "answer": 1,
        "explanation": "S3 Intelligent-Tieringは、アクセスパターンを監視して自動的に最適なストレージクラスに移行します。"
    },
    {
        "id": 76,
        "question": "S3のマルチパートアップロードの最小パートサイズはどれか。",
        "choices": [
            "1MB",
            "5MB",
            "10MB",
            "100MB"
        ],
        "answer": 1,
        "explanation": "S3マルチパートアップロードでは、最後のパートを除いて各パートは最小5MBである必要があります。"
    },
    {
        "id": 77,
        "question": "S3 Select の主な利点はどれか。",
        "choices": [
            "オブジェクト全体をダウンロードせずに必要なデータのみを取得",
            "オブジェクトの暗号化",
            "アクセス制御の強化",
            "ストレージコストの削減"
        ],
        "answer": 0,
        "explanation": "S3 Selectを使用すると、SQLクエリでオブジェクトの一部のみを取得でき、データ転送量とコストを削減できます。"
    },
    {
        "id": 78,
        "question": "S3のアクセスログに記録されない情報はどれか。",
        "choices": [
            "リクエスト時刻",
            "リクエスト元IPアドレス",
            "オブジェクトの内容",
            "HTTPステータスコード"
        ],
        "answer": 2,
        "explanation": "S3アクセスログには、リクエストの詳細情報は記録されますが、オブジェクトの実際の内容は記録されません。"
    },
    {
        "id": 79,
        "question": "S3 Transfer Accelerationが使用するネットワークはどれか。",
        "choices": [
            "AWS Direct Connect",
            "CloudFrontエッジロケーション",
            "VPC Peering",
            "AWS PrivateLink"
        ],
        "answer": 1,
        "explanation": "S3 Transfer AccelerationはCloudFrontのエッジロケーションを利用してアップロード速度を向上させます。"
    },
    {
        "id": 80,
        "question": "S3バケットポリシーとIAMポリシーの違いとして正しいものはどれか。",
        "choices": [
            "バケットポリシーはリソースベース、IAMポリシーはユーザーベース",
            "バケットポリシーはユーザーベース、IAMポリシーはリソースベース",
            "両方ともリソースベース",
            "両方ともユーザーベース"
        ],
        "answer": 0,
        "explanation": "S3バケットポリシーはリソースベースのポリシーで、IAMポリシーはユーザーやロールに適用されるユーザーベースのポリシーです。"
    }
]    # RDS・デ
ータベース詳細問題 (81-100)
    {
        "id": 81,
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
        "id": 82,
        "question": "RDS Read Replicaの制限として正しいものはどれか。",
        "choices": [
            "読み取り専用アクセスのみ",
            "同じリージョン内でのみ作成可能",
            "1つのマスターDBに対して1つのみ作成可能",
            "自動フェイルオーバー機能がある"
        ],
        "answer": 0,
        "explanation": "Read Replicaは読み取り専用で、書き込み操作はマスターDBでのみ実行できます。"
    },
    {
        "id": 83,
        "question": "Amazon Auroraの特徴として正しくないものはどれか。",
        "choices": [
            "MySQL・PostgreSQLと互換性がある",
            "ストレージが自動的にスケールする",
            "NoSQLデータベースである",
            "高可用性を提供する"
        ],
        "answer": 2,
        "explanation": "Amazon Auroraは、MySQL・PostgreSQL互換のリレーショナルデータベースで、NoSQLではありません。"
    },
    {
        "id": 84,
        "question": "DynamoDBのプライマリキーの種類として正しくないものはどれか。",
        "choices": [
            "Partition Key",
            "Composite Key",
            "Foreign Key",
            "Sort Key"
        ],
        "answer": 2,
        "explanation": "DynamoDBはNoSQLデータベースで、Foreign Keyの概念はありません。"
    },
    {
        "id": 85,
        "question": "DynamoDB Global Tablesの説明として正しいものはどれか。",
        "choices": [
            "単一リージョン内でのレプリケーション",
            "複数リージョン間でのマルチマスターレプリケーション",
            "読み取り専用レプリカ",
            "手動同期が必要"
        ],
        "answer": 1,
        "explanation": "DynamoDB Global Tablesは、複数リージョン間でマルチマスターレプリケーションを提供します。"
    },
    {
        "id": 86,
        "question": "Amazon ElastiCacheのクラスターモードの利点はどれか。",
        "choices": [
            "コストの削減",
            "水平スケーリングとデータ分散",
            "セキュリティの向上",
            "バックアップの自動化"
        ],
        "answer": 1,
        "explanation": "ElastiCacheのクラスターモードでは、データを複数のシャードに分散して水平スケーリングが可能です。"
    },
    {
        "id": 87,
        "question": "RDSのメンテナンスウィンドウで実行される作業として正しくないものはどれか。",
        "choices": [
            "OSパッチの適用",
            "データベースエンジンのアップグレード",
            "アプリケーションコードの更新",
            "セキュリティパッチの適用"
        ],
        "answer": 2,
        "explanation": "メンテナンスウィンドウでは、インフラレベルの更新が行われますが、アプリケーションコードの更新は含まれません。"
    },
    {
        "id": 88,
        "question": "DynamoDB Accelerator (DAX)の主な機能はどれか。",
        "choices": [
            "データの暗号化",
            "インメモリキャッシング",
            "データのバックアップ",
            "アクセス制御"
        ],
        "answer": 1,
        "explanation": "DAXは、DynamoDB用のフルマネージドインメモリキャッシュサービスです。"
    },
    {
        "id": 89,
        "question": "Amazon Redshiftのデータ圧縮について正しい説明はどれか。",
        "choices": [
            "手動で設定する必要がある",
            "自動的に最適な圧縮方式を選択する",
            "圧縮は利用できない",
            "追加料金が発生する"
        ],
        "answer": 1,
        "explanation": "Redshiftは、データの特性に基づいて自動的に最適な圧縮方式を選択します。"
    },
    {
        "id": 90,
        "question": "RDSのパフォーマンスインサイトで監視できる項目として正しくないものはどれか。",
        "choices": [
            "CPU使用率",
            "データベース接続数",
            "アプリケーションのレスポンス時間",
            "待機イベント"
        ],
        "answer": 2,
        "explanation": "パフォーマンスインサイトは、データベースレベルのメトリクスを監視しますが、アプリケーションレベルのレスポンス時間は監視しません。"
    },

    # VPC・ネットワーキング詳細問題 (91-110)
    {
        "id": 91,
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
        "id": 92,
        "question": "VPC Peeringの制限として正しいものはどれか。",
        "choices": [
            "同じリージョン内でのみ可能",
            "推移的ルーティングはサポートされない",
            "同じAWSアカウント内でのみ可能",
            "最大2つのVPCまで接続可能"
        ],
        "answer": 1,
        "explanation": "VPC Peeringでは推移的ルーティングはサポートされず、直接接続されたVPC間でのみ通信が可能です。"
    },
    {
        "id": 93,
        "question": "NATゲートウェイとNATインスタンスの違いとして正しいものはどれか。",
        "choices": [
            "NATゲートウェイは手動管理が必要",
            "NATインスタンスはマネージドサービス",
            "NATゲートウェイは高可用性を提供",
            "NATインスタンスの方が高性能"
        ],
        "answer": 2,
        "explanation": "NATゲートウェイはマネージドサービスで、自動的に高可用性を提供します。"
    },
    {
        "id": 94,
        "question": "VPC Endpointの種類として正しくないものはどれか。",
        "choices": [
            "Gateway Endpoint",
            "Interface Endpoint",
            "Network Endpoint",
            "PrivateLink Endpoint"
        ],
        "answer": 2,
        "explanation": "VPC Endpointには、Gateway EndpointとInterface Endpoint（PrivateLink）の2種類があります。"
    },
    {
        "id": 95,
        "question": "セキュリティグループとNACLの違いとして正しいものはどれか。",
        "choices": [
            "セキュリティグループはステートフル、NACLはステートレス",
            "セキュリティグループはステートレス、NACLはステートフル",
            "両方ともステートフル",
            "両方ともステートレス"
        ],
        "answer": 0,
        "explanation": "セキュリティグループはステートフルで、NACLはステートレスです。"
    },
    {
        "id": 96,
        "question": "Elastic IPアドレスの特徴として正しくないものはどれか。",
        "choices": [
            "静的なパブリックIPアドレス",
            "インスタンス間で移動可能",
            "使用していない場合は無料",
            "リージョン内で利用可能"
        ],
        "answer": 2,
        "explanation": "Elastic IPアドレスは、使用していない場合（インスタンスに関連付けられていない場合）は料金が発生します。"
    },
    {
        "id": 97,
        "question": "AWS Direct Connectの仮想インターフェース（VIF）の種類として正しくないものはどれか。",
        "choices": [
            "Private VIF",
            "Public VIF",
            "Transit VIF",
            "Dedicated VIF"
        ],
        "answer": 3,
        "explanation": "Direct Connectの仮想インターフェースには、Private VIF、Public VIF、Transit VIFの3種類があります。"
    },
    {
        "id": 98,
        "question": "VPC Flow Logsで記録される情報として正しくないものはどれか。",
        "choices": [
            "送信元・送信先IPアドレス",
            "ポート番号",
            "パケットの内容",
            "アクション（ACCEPT/REJECT）"
        ],
        "answer": 2,
        "explanation": "VPC Flow Logsは、ネットワークトラフィックのメタデータを記録しますが、パケットの実際の内容は記録しません。"
    },
    {
        "id": 99,
        "question": "AWS PrivateLinkの主な利点はどれか。",
        "choices": [
            "コストの削減",
            "インターネットを経由しないプライベート接続",
            "パフォーマンスの向上",
            "設定の簡素化"
        ],
        "answer": 1,
        "explanation": "AWS PrivateLinkは、インターネットを経由せずにAWSサービスやVPC間でプライベート接続を提供します。"
    },
    {
        "id": 100,
        "question": "VPCのDHCPオプションセットで設定できない項目はどれか。",
        "choices": [
            "ドメイン名",
            "DNSサーバー",
            "NTPサーバー",
            "デフォルトゲートウェイ"
        ],
        "answer": 3,
        "explanation": "DHCPオプションセットでは、デフォルトゲートウェイは設定できません。これはVPCルーターによって自動的に提供されます。"
    }
]   
 # IAM・セキュリティ詳細問題 (101-130)
    {
        "id": 101,
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
    {
        "id": 102,
        "question": "IAM Roleの一時的な認証情報の有効期限として設定できる最大時間はどれか。",
        "choices": [
            "1時間",
            "12時間",
            "24時間",
            "36時間"
        ],
        "answer": 2,
        "explanation": "IAM Roleの一時的な認証情報は、最大12時間（デフォルト1時間）まで設定できます。"
    },
    {
        "id": 103,
        "question": "AWS STS（Security Token Service）の主な機能はどれか。",
        "choices": [
            "永続的な認証情報の発行",
            "一時的な認証情報の発行",
            "パスワードの管理",
            "アクセスログの記録"
        ],
        "answer": 1,
        "explanation": "AWS STSは、一時的なセキュリティ認証情報を発行するサービスです。"
    },
    {
        "id": 104,
        "question": "IAMユーザーのアクセスキーについて正しい説明はどれか。",
        "choices": [
            "1つのユーザーに対して1つのみ作成可能",
            "1つのユーザーに対して最大2つまで作成可能",
            "無制限に作成可能",
            "作成後は変更できない"
        ],
        "answer": 1,
        "explanation": "IAMユーザーは、最大2つのアクセスキーを同時に持つことができます。"
    },
    {
        "id": 105,
        "question": "AWS CloudTrailのログファイルの整合性検証機能の目的はどれか。",
        "choices": [
            "ログファイルの圧縮",
            "ログファイルの改ざん検出",
            "ログファイルの暗号化",
            "ログファイルの自動削除"
        ],
        "answer": 1,
        "explanation": "CloudTrailのログファイル整合性検証は、ログファイルが改ざんされていないことを確認するための機能です。"
    },
    {
        "id": 106,
        "question": "AWS Configのコンプライアンスルールについて正しい説明はどれか。",
        "choices": [
            "リソースの設定変更を自動的に修正する",
            "リソースの設定がルールに準拠しているかを評価する",
            "リソースの作成を制限する",
            "リソースのアクセス権限を管理する"
        ],
        "answer": 1,
        "explanation": "AWS Configルールは、リソースの設定がコンプライアンス要件に準拠しているかを評価します。"
    },
    {
        "id": 107,
        "question": "AWS GuardDutyが検出する脅威の種類として正しくないものはどれか。",
        "choices": [
            "不正なAPIコール",
            "マルウェア感染",
            "アプリケーションの脆弱性",
            "異常なネットワーク通信"
        ],
        "answer": 2,
        "explanation": "GuardDutyは、ネットワークレベルやAPIレベルの脅威を検出しますが、アプリケーションの脆弱性は検出しません。"
    },
    {
        "id": 108,
        "question": "AWS Security Hubの主な機能はどれか。",
        "choices": [
            "セキュリティ脅威の自動修復",
            "セキュリティ検出結果の一元管理",
            "ネットワークトラフィックの監視",
            "アクセス権限の管理"
        ],
        "answer": 1,
        "explanation": "Security Hubは、複数のセキュリティサービスからの検出結果を一元的に管理・表示するサービスです。"
    },
    {
        "id": 109,
        "question": "AWS KMSのカスタマーマネージドキーの特徴として正しくないものはどれか。",
        "choices": [
            "キーの作成・管理が可能",
            "キーローテーションの設定が可能",
            "無料で利用できる",
            "キーポリシーの設定が可能"
        ],
        "answer": 2,
        "explanation": "カスタマーマネージドキーは有料サービスで、キーの使用量に応じて料金が発生します。"
    },
    {
        "id": 110,
        "question": "AWS Certificate Manager (ACM)で管理される証明書の自動更新について正しい説明はどれか。",
        "choices": [
            "すべての証明書が自動更新される",
            "AWSサービスで使用される証明書のみ自動更新される",
            "手動で更新する必要がある",
            "有料オプションで自動更新が可能"
        ],
        "answer": 1,
        "explanation": "ACMで発行された証明書は、AWSサービス（CloudFront、ELB等）で使用される場合のみ自動更新されます。"
    },
    {
        "id": 111,
        "question": "AWS WAFのルールタイプとして正しくないものはどれか。",
        "choices": [
            "Rate-based rules",
            "Regular rules",
            "Managed rules",
            "Custom rules"
        ],
        "answer": 3,
        "explanation": "AWS WAFには、Rate-based rules、Regular rules、Managed rulesがありますが、Custom rulesという分類はありません。"
    },
    {
        "id": 112,
        "question": "AWS Shieldの2つのレベルの違いとして正しいものはどれか。",
        "choices": [
            "StandardとAdvanced",
            "BasicとPremium",
            "FreeとPaid",
            "LiteとPro"
        ],
        "answer": 0,
        "explanation": "AWS Shieldには、Shield Standard（無料）とShield Advanced（有料）の2つのレベルがあります。"
    },
    {
        "id": 113,
        "question": "AWS Systems Manager Session Managerの利点として正しくないものはどれか。",
        "choices": [
            "SSHキーが不要",
            "セッションログの記録",
            "インターネット接続が不要",
            "パフォーマンスの向上"
        ],
        "answer": 3,
        "explanation": "Session Managerは、セキュアなアクセスとログ記録を提供しますが、パフォーマンス向上が主な目的ではありません。"
    },
    {
        "id": 114,
        "question": "AWS Secrets Managerの自動ローテーション機能について正しい説明はどれか。",
        "choices": [
            "すべてのシークレットで利用可能",
            "特定のデータベースエンジンでのみ利用可能",
            "手動設定が必要",
            "追加料金は発生しない"
        ],
        "answer": 1,
        "explanation": "Secrets Managerの自動ローテーションは、サポートされている特定のデータベースエンジン（RDS等）でのみ利用可能です。"
    },
    {
        "id": 115,
        "question": "AWS CloudHSMの特徴として正しいものはどれか。",
        "choices": [
            "ソフトウェアベースの暗号化",
            "ハードウェアベースの暗号化",
            "無料で利用可能",
            "自動的にスケールする"
        ],
        "answer": 1,
        "explanation": "AWS CloudHSMは、FIPS 140-2 Level 3認定のハードウェアセキュリティモジュールを提供します。"
    },

    # Lambda・サーバーレス詳細問題 (116-140)
    {
        "id": 116,
        "question": "AWS Lambda関数のメモリ設定の範囲はどれか。",
        "choices": [
            "128MB - 1GB",
            "128MB - 3GB",
            "128MB - 10GB",
            "256MB - 3GB"
        ],
        "answer": 2,
        "explanation": "Lambda関数のメモリは、128MBから10,240MB（10GB）まで設定できます。"
    },
    {
        "id": 117,
        "question": "Lambda関数の同時実行数のデフォルト制限はどれか。",
        "choices": [
            "100",
            "500",
            "1000",
            "制限なし"
        ],
        "answer": 2,
        "explanation": "Lambda関数の同時実行数のデフォルト制限は、リージョンあたり1000です。"
    },
    {
        "id": 118,
        "question": "Lambda Layersの主な用途はどれか。",
        "choices": [
            "関数のパフォーマンス向上",
            "共通ライブラリやコードの共有",
            "セキュリティの強化",
            "コストの削減"
        ],
        "answer": 1,
        "explanation": "Lambda Layersは、複数の関数間で共通のライブラリやコードを共有するために使用されます。"
    },
    {
        "id": 119,
        "question": "Lambda関数のコールドスタートを軽減する方法として正しくないものはどれか。",
        "choices": [
            "Provisioned Concurrencyの使用",
            "関数のメモリ増加",
            "定期的な関数呼び出し",
            "関数の実行時間延長"
        ],
        "answer": 3,
        "explanation": "実行時間の延長は、コールドスタートの軽減には効果がありません。"
    },
    {
        "id": 120,
        "question": "AWS Step Functionsのワークフロー定義に使用される言語はどれか。",
        "choices": [
            "JSON",
            "YAML",
            "Amazon States Language (ASL)",
            "XML"
        ],
        "answer": 2,
        "explanation": "Step Functionsでは、Amazon States Language（ASL）というJSON形式の言語を使用してワークフローを定義します。"
    },
    {
        "id": 121,
        "question": "Amazon API Gatewayの認証方法として正しくないものはどれか。",
        "choices": [
            "IAM認証",
            "Cognito User Pools",
            "Lambda Authorizer",
            "Active Directory"
        ],
        "answer": 3,
        "explanation": "API Gatewayは、Active Directoryを直接サポートしていません。Cognitoを通じて統合する必要があります。"
    },
    {
        "id": 122,
        "question": "Lambda関数の環境変数について正しい説明はどれか。",
        "choices": [
            "実行時に変更可能",
            "デプロイ時に設定され、実行時は読み取り専用",
            "暗号化できない",
            "最大10個まで設定可能"
        ],
        "answer": 1,
        "explanation": "Lambda関数の環境変数は、デプロイ時に設定され、実行時は読み取り専用です。"
    },
    {
        "id": 123,
        "question": "AWS SAM（Serverless Application Model）の説明として正しいものはどれか。",
        "choices": [
            "サーバーレスアプリケーションの実行環境",
            "サーバーレスアプリケーションの定義・デプロイフレームワーク",
            "サーバーレスアプリケーションの監視ツール",
            "サーバーレスアプリケーションのテストツール"
        ],
        "answer": 1,
        "explanation": "AWS SAMは、サーバーレスアプリケーションを定義・デプロイするためのフレームワークです。"
    },
    {
        "id": 124,
        "question": "Lambda関数のデッドレターキュー（DLQ）の目的はどれか。",
        "choices": [
            "パフォーマンスの向上",
            "失敗したイベントの処理",
            "セキュリティの強化",
            "コストの削減"
        ],
        "answer": 1,
        "explanation": "デッドレターキューは、処理に失敗したイベントを別のキューに送信して、後で分析や再処理を行うために使用されます。"
    },
    {
        "id": 125,
        "question": "Amazon EventBridgeのカスタムイベントバスの利点はどれか。",
        "choices": [
            "コストの削減",
            "イベントの分離と組織化",
            "パフォーマンスの向上",
            "セキュリティの自動化"
        ],
        "answer": 1,
        "explanation": "カスタムイベントバスを使用することで、異なるアプリケーションやサービスのイベントを分離して組織化できます。"
    },

    # CloudWatch・監視詳細問題 (126-150)
    {
        "id": 126,
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
        "id": 127,
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
        "id": 128,
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
        "id": 129,
        "question": "CloudWatch Dashboardで表示できないウィジェットタイプはどれか。",
        "choices": [
            "Line chart",
            "Number",
            "Log insights",
            "Video stream"
        ],
        "answer": 3,
        "explanation": "CloudWatch Dashboardでは、メトリクス、ログ、テキストなどのウィジェットを表示できますが、ビデオストリームは表示できません。"
    },
    {
        "id": 130,
        "question": "CloudWatch Eventsの後継サービスはどれか。",
        "choices": [
            "CloudWatch Logs",
            "EventBridge",
            "SNS",
            "SQS"
        ],
        "answer": 1,
        "explanation": "CloudWatch Eventsは、Amazon EventBridgeに統合され、EventBridgeがその後継サービスです。"
    }
]    # 
コスト管理・請求詳細問題 (131-160)
    {
        "id": 131,
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
        "id": 132,
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
    {
        "id": 133,
        "question": "Reserved Instancesの支払いオプションとして正しくないものはどれか。",
        "choices": [
            "No Upfront",
            "Partial Upfront",
            "All Upfront",
            "Monthly Payment"
        ],
        "answer": 3,
        "explanation": "Reserved Instancesの支払いオプションは、No Upfront、Partial Upfront、All Upfrontの3つです。"
    },
    {
        "id": 134,
        "question": "AWS Savings Plansの種類として正しくないものはどれか。",
        "choices": [
            "Compute Savings Plans",
            "EC2 Instance Savings Plans",
            "Storage Savings Plans",
            "SageMaker Savings Plans"
        ],
        "answer": 2,
        "explanation": "Savings Plansには、Compute、EC2 Instance、SageMakerの3種類がありますが、Storage Savings Plansはありません。"
    },
    {
        "id": 135,
        "question": "AWS Cost Explorerのデフォルトのデータ保持期間はどれか。",
        "choices": [
            "6か月",
            "12か月",
            "18か月",
            "24か月"
        ],
        "answer": 1,
        "explanation": "Cost Explorerでは、デフォルトで過去12か月のコストデータを表示できます。"
    },
    {
        "id": 136,
        "question": "AWS Organizations の統合請求機能の利点として正しくないものはどれか。",
        "choices": [
            "ボリュームディスカウントの適用",
            "請求書の一元化",
            "アカウント間でのリザーブドインスタンス共有",
            "自動的なコスト最適化"
        ],
        "answer": 3,
        "explanation": "統合請求は請求の一元化とボリュームディスカウントを提供しますが、自動的なコスト最適化は行いません。"
    },
    {
        "id": 137,
        "question": "AWS Pricing Calculatorの主な用途はどれか。",
        "choices": [
            "実際のコストの監視",
            "将来のコスト予測",
            "サービス利用前のコスト見積もり",
            "コスト最適化の推奨事項"
        ],
        "answer": 2,
        "explanation": "AWS Pricing Calculatorは、AWSサービスを利用する前にコストを見積もるためのツールです。"
    },
    {
        "id": 138,
        "question": "AWS Cost Anomaly Detectionの機能はどれか。",
        "choices": [
            "予算の自動設定",
            "異常なコスト増加の検出",
            "リソースの自動削除",
            "料金の自動支払い"
        ],
        "answer": 1,
        "explanation": "Cost Anomaly Detectionは、機械学習を使用して異常なコスト増加を検出し、アラートを送信します。"
    },
    {
        "id": 139,
        "question": "AWS Free Tierの種類として正しくないものはどれか。",
        "choices": [
            "Always Free",
            "12 Months Free",
            "Trials",
            "Enterprise Free"
        ],
        "answer": 3,
        "explanation": "AWS Free Tierには、Always Free、12 Months Free、Trialsの3種類がありますが、Enterprise Freeはありません。"
    },
    {
        "id": 140,
        "question": "AWS Marketplace での購入について正しい説明はどれか。",
        "choices": [
            "すべて無料で利用できる",
            "AWS請求書に統合される",
            "別途契約が必要",
            "クレジットカードでのみ支払い可能"
        ],
        "answer": 1,
        "explanation": "AWS Marketplaceでの購入は、AWS請求書に統合され、既存のAWS支払い方法で決済されます。"
    },

    # 高度なサービス・新サービス問題 (141-200)
    {
        "id": 141,
        "question": "Amazon SageMakerの主な用途はどれか。",
        "choices": [
            "Webアプリケーションのホスティング",
            "機械学習モデルの構築・訓練・デプロイ",
            "データベースの管理",
            "ネットワークの監視"
        ],
        "answer": 1,
        "explanation": "Amazon SageMakerは、機械学習モデルの構築、訓練、デプロイを行うフルマネージドサービスです。"
    },
    {
        "id": 142,
        "question": "AWS Glueの説明として正しいものはどれか。",
        "choices": [
            "データベース管理サービス",
            "ETL（Extract, Transform, Load）サービス",
            "ファイル転送サービス",
            "バックアップサービス"
        ],
        "answer": 1,
        "explanation": "AWS Glueは、データの抽出、変換、ロードを行うフルマネージドETLサービスです。"
    },
    {
        "id": 143,
        "question": "Amazon Athenaでクエリできるデータソースとして正しくないものはどれか。",
        "choices": [
            "Amazon S3",
            "Amazon DynamoDB",
            "Amazon RDS",
            "AWS CloudTrail logs"
        ],
        "answer": 2,
        "explanation": "Athenaは主にS3上のデータに対してクエリを実行しますが、RDSに直接クエリすることはできません。"
    },
    {
        "id": 144,
        "question": "Amazon QuickSightの主な機能はどれか。",
        "choices": [
            "データベース管理",
            "ビジネスインテリジェンス・データ可視化",
            "機械学習モデル訓練",
            "ネットワーク監視"
        ],
        "answer": 1,
        "explanation": "Amazon QuickSightは、ビジネスインテリジェンスとデータ可視化のためのサービスです。"
    },
    {
        "id": 145,
        "question": "AWS Data Pipelineの後継サービスはどれか。",
        "choices": [
            "AWS Glue",
            "Amazon EMR",
            "AWS Step Functions",
            "Amazon Kinesis"
        ],
        "answer": 0,
        "explanation": "AWS Data Pipelineの機能は、AWS Glueに統合され、Glueが推奨されるETLサービスです。"
    },
    {
        "id": 146,
        "question": "Amazon Comprehendの機能はどれか。",
        "choices": [
            "画像認識",
            "自然言語処理",
            "音声認識",
            "動画解析"
        ],
        "answer": 1,
        "explanation": "Amazon Comprehendは、自然言語処理（NLP）を行うサービスで、テキストの感情分析や言語検出などを提供します。"
    },
    {
        "id": 147,
        "question": "Amazon Rekognitionでできないことはどれか。",
        "choices": [
            "顔認識",
            "オブジェクト検出",
            "音声認識",
            "テキスト検出"
        ],
        "answer": 2,
        "explanation": "Amazon Rekognitionは画像・動画分析サービスで、音声認識は行いません。音声認識はAmazon Transcribeが担当します。"
    },
    {
        "id": 148,
        "question": "Amazon Pollyの機能はどれか。",
        "choices": [
            "音声認識",
            "テキスト読み上げ",
            "画像生成",
            "動画編集"
        ],
        "answer": 1,
        "explanation": "Amazon Pollyは、テキストを自然な音声に変換するテキスト読み上げサービスです。"
    },
    {
        "id": 149,
        "question": "AWS IoT Coreの主な機能はどれか。",
        "choices": [
            "Webアプリケーションのホスティング",
            "IoTデバイスの接続・管理",
            "データベースの管理",
            "ファイルストレージ"
        ],
        "answer": 1,
        "explanation": "AWS IoT Coreは、IoTデバイスをクラウドに安全に接続し、管理するためのサービスです。"
    },
    {
        "id": 150,
        "question": "Amazon WorkSpacesの説明として正しいものはどれか。",
        "choices": [
            "ファイル共有サービス",
            "仮想デスクトップサービス",
            "メール配信サービス",
            "データベースサービス"
        ],
        "answer": 1,
        "explanation": "Amazon WorkSpacesは、クラウドベースの仮想デスクトップサービス（VDI）です。"
    },
    {
        "id": 151,
        "question": "AWS AppSyncの主な機能はどれか。",
        "choices": [
            "ファイル同期",
            "GraphQL APIの管理",
            "データベース同期",
            "アプリケーション配布"
        ],
        "answer": 1,
        "explanation": "AWS AppSyncは、GraphQL APIを簡単に構築・管理できるサービスです。"
    },
    {
        "id": 152,
        "question": "Amazon Cognitoの2つの主要コンポーネントはどれか。",
        "choices": [
            "User PoolsとIdentity Pools",
            "Auth PoolsとAccess Pools",
            "Login PoolsとToken Pools",
            "Session PoolsとCredential Pools"
        ],
        "answer": 0,
        "explanation": "Amazon Cognitoは、User Pools（ユーザー認証）とIdentity Pools（フェデレーテッドアイデンティティ）の2つの主要コンポーネントで構成されています。"
    },
    {
        "id": 153,
        "question": "AWS Amplifyの説明として正しいものはどれか。",
        "choices": [
            "データベース管理サービス",
            "フルスタックアプリケーション開発プラットフォーム",
            "ネットワーク監視サービス",
            "バックアップサービス"
        ],
        "answer": 1,
        "explanation": "AWS Amplifyは、モバイルアプリやWebアプリケーションを迅速に構築・デプロイするためのフルスタック開発プラットフォームです。"
    },
    {
        "id": 154,
        "question": "Amazon Pinpointの主な用途はどれか。",
        "choices": [
            "データベース管理",
            "顧客エンゲージメント・マーケティング",
            "ネットワーク監視",
            "ファイル管理"
        ],
        "answer": 1,
        "explanation": "Amazon Pinpointは、顧客エンゲージメントとマーケティングコミュニケーションのためのサービスです。"
    },
    {
        "id": 155,
        "question": "AWS Device Farmの機能はどれか。",
        "choices": [
            "IoTデバイス管理",
            "モバイルアプリケーションテスト",
            "サーバー監視",
            "データ分析"
        ],
        "answer": 1,
        "explanation": "AWS Device Farmは、実際のデバイス上でモバイルアプリケーションをテストするサービスです。"
    },
    {
        "id": 156,
        "question": "Amazon GameLiftの用途はどれか。",
        "choices": [
            "Webアプリケーションホスティング",
            "ゲームサーバーホスティング",
            "データベース管理",
            "ファイルストレージ"
        ],
        "answer": 1,
        "explanation": "Amazon GameLiftは、マルチプレイヤーゲーム用の専用ゲームサーバーホスティングサービスです。"
    },
    {
        "id": 157,
        "question": "AWS Ground Stationの機能はどれか。",
        "choices": [
            "地上局サービス",
            "衛星通信サービス",
            "GPS追跡サービス",
            "気象データサービス"
        ],
        "answer": 1,
        "explanation": "AWS Ground Stationは、衛星との通信を行うためのフルマネージド地上局サービスです。"
    },
    {
        "id": 158,
        "question": "Amazon Braketの説明として正しいものはどれか。",
        "choices": [
            "機械学習サービス",
            "量子コンピューティングサービス",
            "ブロックチェーンサービス",
            "AR/VRサービス"
        ],
        "answer": 1,
        "explanation": "Amazon Braketは、量子コンピューティングの研究開発を支援するサービスです。"
    },
    {
        "id": 159,
        "question": "AWS Honeycodeの機能はどれか。",
        "choices": [
            "セキュリティ監視",
            "ノーコードアプリケーション開発",
            "データベース管理",
            "ネットワーク分析"
        ],
        "answer": 1,
        "explanation": "AWS Honeycodeは、プログラミング知識なしでアプリケーションを構築できるノーコード開発プラットフォームです。"
    },
    {
        "id": 160,
        "question": "Amazon Nimble Studioの用途はどれか。",
        "choices": [
            "Webアプリケーション開発",
            "クリエイティブコンテンツ制作",
            "データ分析",
            "IoTデバイス管理"
        ],
        "answer": 1,
        "explanation": "Amazon Nimble Studioは、映画、テレビ、ゲームなどのクリエイティブコンテンツ制作のためのクラウドスタジオサービスです。"
    }
]   
 # 運用・管理・DevOps問題 (161-200)
    {
        "id": 161,
        "question": "AWS CodeCommitの説明として正しいものはどれか。",
        "choices": [
            "継続的インテグレーションサービス",
            "プライベートGitリポジトリサービス",
            "アプリケーションデプロイサービス",
            "コード品質分析サービス"
        ],
        "answer": 1,
        "explanation": "AWS CodeCommitは、フルマネージドなプライベートGitリポジトリホスティングサービスです。"
    },
    {
        "id": 162,
        "question": "AWS CodeBuildの課金モデルはどれか。",
        "choices": [
            "月額固定料金",
            "ビルド実行時間に基づく従量課金",
            "リポジトリ数に基づく課金",
            "無料で利用可能"
        ],
        "answer": 1,
        "explanation": "CodeBuildは、ビルドの実行時間（分単位）に基づいて課金されます。"
    },
    {
        "id": 163,
        "question": "AWS CodeDeployでサポートされていないデプロイ先はどれか。",
        "choices": [
            "EC2インスタンス",
            "Lambda関数",
            "ECS サービス",
            "RDS データベース"
        ],
        "answer": 3,
        "explanation": "CodeDeployは、EC2、Lambda、ECSへのデプロイをサポートしていますが、RDSデータベースはサポートしていません。"
    },
    {
        "id": 164,
        "question": "AWS CodePipelineのステージで実行できないアクションはどれか。",
        "choices": [
            "ソースコードの取得",
            "ビルドの実行",
            "テストの実行",
            "データベースのバックアップ"
        ],
        "answer": 3,
        "explanation": "CodePipelineは、CI/CDパイプラインのためのサービスで、データベースバックアップのような運用タスクは直接実行できません。"
    },
    {
        "id": 165,
        "question": "AWS Systems Manager Patch Managerの機能はどれか。",
        "choices": [
            "アプリケーションの更新",
            "OSパッチの管理",
            "データベースの更新",
            "ネットワーク設定の更新"
        ],
        "answer": 1,
        "explanation": "Patch Managerは、EC2インスタンスやオンプレミスサーバーのOSパッチを自動的に管理するサービスです。"
    },
    {
        "id": 166,
        "question": "AWS OpsWorksで使用されるオーケストレーションツールはどれか。",
        "choices": [
            "Ansible",
            "Chef",
            "Puppet",
            "Terraform"
        ],
        "answer": 1,
        "explanation": "AWS OpsWorksは、ChefとPuppetを使用したアプリケーション管理サービスです。"
    },
    {
        "id": 167,
        "question": "AWS Service Catalogの主な目的はどれか。",
        "choices": [
            "サービスの価格比較",
            "承認されたITサービスの管理・配布",
            "サービスの監視",
            "サービスの自動スケーリング"
        ],
        "answer": 1,
        "explanation": "Service Catalogは、組織が承認したITサービスやリソースをカタログとして管理・配布するサービスです。"
    },
    {
        "id": 168,
        "question": "AWS Personal Health Dashboardの機能はどれか。",
        "choices": [
            "個人の健康管理",
            "AWSサービスの個別影響通知",
            "アプリケーションの健康状態監視",
            "ネットワークの健康状態監視"
        ],
        "answer": 1,
        "explanation": "Personal Health Dashboardは、AWSサービスの問題が個人のリソースに与える影響を通知するサービスです。"
    },
    {
        "id": 169,
        "question": "AWS Trusted Advisorのチェック項目として含まれないものはどれか。",
        "choices": [
            "コスト最適化",
            "セキュリティ",
            "パフォーマンス",
            "アプリケーションコード品質"
        ],
        "answer": 3,
        "explanation": "Trusted Advisorは、インフラレベルの推奨事項を提供しますが、アプリケーションコードの品質チェックは行いません。"
    },
    {
        "id": 170,
        "question": "AWS Well-Architected Toolの目的はどれか。",
        "choices": [
            "アーキテクチャの自動構築",
            "アーキテクチャのベストプラクティス評価",
            "アーキテクチャの監視",
            "アーキテクチャのコスト計算"
        ],
        "answer": 1,
        "explanation": "Well-Architected Toolは、アーキテクチャがAWSのベストプラクティスに従っているかを評価するためのツールです。"
    },
    {
        "id": 171,
        "question": "Amazon CloudWatchのカスタムメトリクスの送信方法はどれか。",
        "choices": [
            "AWS CLI",
            "AWS SDK",
            "CloudWatch API",
            "すべて正しい"
        ],
        "answer": 3,
        "explanation": "カスタムメトリクスは、AWS CLI、SDK、CloudWatch APIのいずれの方法でも送信できます。"
    },
    {
        "id": 172,
        "question": "AWS Config Rulesの評価トリガーとして正しくないものはどれか。",
        "choices": [
            "設定変更時",
            "定期的な評価",
            "手動実行",
            "コスト変更時"
        ],
        "answer": 3,
        "explanation": "Config Rulesは、リソースの設定変更、定期評価、手動実行でトリガーされますが、コスト変更では評価されません。"
    },
    {
        "id": 173,
        "question": "AWS CloudTrailのデータイベントで記録される操作はどれか。",
        "choices": [
            "IAMユーザーの作成",
            "S3オブジェクトの読み取り・書き込み",
            "EC2インスタンスの起動",
            "VPCの作成"
        ],
        "answer": 1,
        "explanation": "データイベントは、S3オブジェクトやLambda関数の実行など、リソース内での操作を記録します。"
    },
    {
        "id": 174,
        "question": "AWS Systems Manager Run Commandの実行対象として正しくないものはどれか。",
        "choices": [
            "EC2インスタンス",
            "オンプレミスサーバー",
            "Lambda関数",
            "Systems Manager管理下のサーバー"
        ],
        "answer": 2,
        "explanation": "Run Commandは、EC2インスタンスやオンプレミスサーバーでコマンドを実行しますが、Lambda関数では実行できません。"
    },
    {
        "id": 175,
        "question": "AWS Auto Scalingの予測スケーリングの特徴はどれか。",
        "choices": [
            "過去のメトリクスに基づく事前スケーリング",
            "リアルタイムメトリクスに基づくスケーリング",
            "手動でのスケーリング",
            "固定スケジュールでのスケーリング"
        ],
        "answer": 0,
        "explanation": "予測スケーリングは、過去のトラフィックパターンを機械学習で分析し、需要を予測して事前にスケーリングを行います。"
    },
    {
        "id": 176,
        "question": "Amazon EventBridgeのルールで設定できないターゲットはどれか。",
        "choices": [
            "Lambda関数",
            "SQSキュー",
            "SNSトピック",
            "RDSデータベース"
        ],
        "answer": 3,
        "explanation": "EventBridgeは、Lambda、SQS、SNSなど多くのAWSサービスをターゲットにできますが、RDSデータベースは直接ターゲットにできません。"
    },
    {
        "id": 177,
        "question": "AWS Resource Groupsの主な用途はどれか。",
        "choices": [
            "リソースの論理的なグループ化",
            "リソースの物理的な配置",
            "リソースの暗号化",
            "リソースの自動削除"
        ],
        "answer": 0,
        "explanation": "Resource Groupsは、タグやその他の基準に基づいてAWSリソースを論理的にグループ化するサービスです。"
    },
    {
        "id": 178,
        "question": "AWS License Managerの機能はどれか。",
        "choices": [
            "AWSサービスのライセンス管理",
            "サードパーティソフトウェアライセンスの管理",
            "オープンソースライセンスの管理",
            "すべて正しい"
        ],
        "answer": 1,
        "explanation": "License Managerは、Microsoft、Oracle、SAP等のサードパーティソフトウェアライセンスを管理するサービスです。"
    },
    {
        "id": 179,
        "question": "AWS Control Towerのガードレールの種類として正しくないものはどれか。",
        "choices": [
            "Preventive guardrails",
            "Detective guardrails",
            "Corrective guardrails",
            "Proactive guardrails"
        ],
        "answer": 2,
        "explanation": "Control Towerのガードレールには、Preventive（予防的）、Detective（検出的）、Proactive（予防的）がありますが、Correctiveはありません。"
    },
    {
        "id": 180,
        "question": "AWS Chatbotの統合先として正しくないものはどれか。",
        "choices": [
            "Slack",
            "Microsoft Teams",
            "Amazon Chime",
            "Discord"
        ],
        "answer": 3,
        "explanation": "AWS Chatbotは、Slack、Microsoft Teams、Amazon Chimeと統合できますが、Discordはサポートされていません。"
    },

    # 追加のクラウド概念・アーキテクチャ問題 (181-220)
    {
        "id": 181,
        "question": "クラウドコンピューティングの「弾力性（Elasticity）」の説明として正しいものはどれか。",
        "choices": [
            "システムの耐障害性",
            "需要に応じたリソースの自動調整",
            "データの整合性",
            "ネットワークの安定性"
        ],
        "answer": 1,
        "explanation": "弾力性とは、需要の変化に応じてリソースを自動的にスケールアップ・ダウンできる能力のことです。"
    },
    {
        "id": 182,
        "question": "「Infrastructure as Code (IaC)」の利点として正しくないものはどれか。",
        "choices": [
            "設定の一貫性",
            "バージョン管理",
            "手動作業の削減",
            "ハードウェアコストの削減"
        ],
        "answer": 3,
        "explanation": "IaCは、インフラの管理を自動化・標準化しますが、直接的なハードウェアコスト削減が主な目的ではありません。"
    },
    {
        "id": 183,
        "question": "マイクロサービスアーキテクチャの特徴として正しくないものはどれか。",
        "choices": [
            "サービスの独立性",
            "単一のデータベース使用",
            "個別デプロイ可能",
            "技術スタックの多様性"
        ],
        "answer": 1,
        "explanation": "マイクロサービスでは、各サービスが独自のデータベースを持つことが推奨され、単一のデータベース共有は避けられます。"
    },
    {
        "id": 184,
        "question": "「Serverless」アーキテクチャの特徴として正しいものはどれか。",
        "choices": [
            "サーバーが存在しない",
            "サーバー管理が不要",
            "常時稼働するサーバー",
            "物理サーバーのみ使用"
        ],
        "answer": 1,
        "explanation": "Serverlessは、サーバーが存在しないのではなく、ユーザーがサーバー管理を行う必要がないアーキテクチャです。"
    },
    {
        "id": 185,
        "question": "クラウドネイティブアプリケーションの設計原則として正しくないものはどれか。",
        "choices": [
            "ステートレス設計",
            "モノリシック構造",
            "自動スケーリング",
            "障害に対する回復力"
        ],
        "answer": 1,
        "explanation": "クラウドネイティブアプリケーションは、マイクロサービス構造を採用し、モノリシック構造は避けられます。"
    },
    {
        "id": 186,
        "question": "「12-Factor App」の原則に含まれないものはどれか。",
        "choices": [
            "コードベース",
            "設定",
            "データベース正規化",
            "ログ"
        ],
        "answer": 2,
        "explanation": "12-Factor Appは、クラウドアプリケーションの設計原則で、データベース正規化は含まれません。"
    },
    {
        "id": 187,
        "question": "「Blue-Green Deployment」の利点はどれか。",
        "choices": [
            "コストの削減",
            "ダウンタイムの最小化",
            "開発速度の向上",
            "セキュリティの強化"
        ],
        "answer": 1,
        "explanation": "Blue-Green Deploymentは、2つの同一環境を使用してダウンタイムを最小化するデプロイ戦略です。"
    },
    {
        "id": 188,
        "question": "「Canary Deployment」の説明として正しいものはどれか。",
        "choices": [
            "全ユーザーに一度にデプロイ",
            "一部のユーザーに段階的にデプロイ",
            "開発環境でのみデプロイ",
            "バックアップ環境へのデプロイ"
        ],
        "answer": 1,
        "explanation": "Canary Deploymentは、新バージョンを一部のユーザーに段階的にリリースしてリスクを軽減するデプロイ戦略です。"
    },
    {
        "id": 189,
        "question": "「Circuit Breaker Pattern」の目的はどれか。",
        "choices": [
            "セキュリティの強化",
            "障害の連鎖を防ぐ",
            "パフォーマンスの向上",
            "コストの削減"
        ],
        "answer": 1,
        "explanation": "Circuit Breaker Patternは、依存サービスの障害が連鎖的に広がることを防ぐ設計パターンです。"
    },
    {
        "id": 190,
        "question": "「Event-Driven Architecture」の特徴はどれか。",
        "choices": [
            "同期的な処理",
            "イベントによる非同期通信",
            "単一のデータベース",
            "モノリシック構造"
        ],
        "answer": 1,
        "explanation": "Event-Driven Architectureは、イベントを通じた非同期通信によってサービス間の疎結合を実現します。"
    },
    {
        "id": 191,
        "question": "「CQRS（Command Query Responsibility Segregation）」の説明として正しいものはどれか。",
        "choices": [
            "読み取りと書き込みの責任を分離",
            "データベースの正規化手法",
            "セキュリティパターン",
            "ネットワーク設計パターン"
        ],
        "answer": 0,
        "explanation": "CQRSは、コマンド（書き込み）とクエリ（読み取り）の責任を分離する設計パターンです。"
    },
    {
        "id": 192,
        "question": "「Saga Pattern」が解決する問題はどれか。",
        "choices": [
            "分散システムでのトランザクション管理",
            "データの暗号化",
            "ネットワークの最適化",
            "ユーザー認証"
        ],
        "answer": 0,
        "explanation": "Saga Patternは、マイクロサービス環境での分散トランザクションを管理するための設計パターンです。"
    },
    {
        "id": 193,
        "question": "「API Gateway Pattern」の利点として正しくないものはどれか。",
        "choices": [
            "API の一元管理",
            "認証・認可の統一",
            "データベースの最適化",
            "レート制限の実装"
        ],
        "answer": 2,
        "explanation": "API Gateway Patternは、API管理に関する機能を提供しますが、データベース最適化は直接的な利点ではありません。"
    },
    {
        "id": 194,
        "question": "「Bulkhead Pattern」の目的はどれか。",
        "choices": [
            "パフォーマンスの向上",
            "障害の分離",
            "コストの削減",
            "セキュリティの強化"
        ],
        "answer": 1,
        "explanation": "Bulkhead Patternは、システムの一部の障害が全体に影響しないよう、リソースを分離する設計パターンです。"
    },
    {
        "id": 195,
        "question": "「Strangler Fig Pattern」の用途はどれか。",
        "choices": [
            "新規システム開発",
            "レガシーシステムの段階的移行",
            "データバックアップ",
            "セキュリティ監査"
        ],
        "answer": 1,
        "explanation": "Strangler Fig Patternは、レガシーシステムを段階的に新システムに置き換える際に使用される移行パターンです。"
    },
    {
        "id": 196,
        "question": "「Database per Service Pattern」の利点はどれか。",
        "choices": [
            "データの一貫性保証",
            "サービスの独立性",
            "管理の簡素化",
            "コストの削減"
        ],
        "answer": 1,
        "explanation": "Database per Service Patternは、各マイクロサービスが独自のデータベースを持つことで、サービス間の独立性を確保します。"
    },
    {
        "id": 197,
        "question": "「Retry Pattern」の実装で考慮すべき要素として正しくないものはどれか。",
        "choices": [
            "リトライ回数の制限",
            "指数バックオフ",
            "無限リトライ",
            "ジッター（ランダム遅延）"
        ],
        "answer": 2,
        "explanation": "無限リトライは、システムリソースを枯渇させる可能性があるため、適切なリトライ制限を設ける必要があります。"
    },
    {
        "id": 198,
        "question": "「Sidecar Pattern」の説明として正しいものはどれか。",
        "choices": [
            "メインアプリケーションと並行して動作する補助コンポーネント",
            "データベースのレプリケーション手法",
            "ネットワークの冗長化手法",
            "セキュリティの暗号化手法"
        ],
        "answer": 0,
        "explanation": "Sidecar Patternは、メインアプリケーションと並行して動作し、横断的関心事（ログ、監視等）を処理する補助コンポーネントです。"
    },
    {
        "id": 199,
        "question": "「Ambassador Pattern」の用途はどれか。",
        "choices": [
            "ユーザー認証",
            "外部サービスへのアクセス代理",
            "データ暗号化",
            "ログ管理"
        ],
        "answer": 1,
        "explanation": "Ambassador Patternは、外部サービスへのアクセスを代理し、接続管理やリトライロジックなどを担当します。"
    },
    {
        "id": 200,
        "question": "「Adapter Pattern」がマイクロサービスで使用される場面はどれか。",
        "choices": [
            "異なるインターフェースの統合",
            "データベースの最適化",
            "ネットワークの高速化",
            "セキュリティの強化"
        ],
        "answer": 0,
        "explanation": "Adapter Patternは、異なるインターフェースやプロトコルを持つサービス間の統合を可能にします。"
    }
]