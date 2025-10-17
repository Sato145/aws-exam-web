#!/usr/bin/env python3
"""
AWS試験対策アプリのテストスクリプト
"""

from app import app, exam_data

def test_app():
    """アプリケーションの基本機能をテスト"""
    print("🧪 AWS試験対策アプリのテストを開始します...")
    
    # 問題データのテスト
    questions = exam_data.questions
    print(f"✅ 問題数: {len(questions)}問")
    
    # 各問題の構造をチェック
    for i, q in enumerate(questions[:3]):  # 最初の3問をチェック
        required_keys = ['id', 'question', 'choices', 'answer', 'explanation']
        for key in required_keys:
            if key not in q:
                print(f"❌ 問題{i+1}に{key}が不足しています")
                return False
        
        if len(q['choices']) != 4:
            print(f"❌ 問題{i+1}の選択肢が4つではありません")
            return False
            
        if not (0 <= q['answer'] <= 3):
            print(f"❌ 問題{i+1}の正解番号が無効です")
            return False
    
    print("✅ 問題データの構造チェック完了")
    
    # Flaskアプリのテスト
    with app.test_client() as client:
        # ホームページ
        response = client.get('/')
        if response.status_code != 200:
            print("❌ ホームページの読み込みに失敗")
            return False
        print("✅ ホームページ正常")
        
        # 試験ページ
        response = client.get('/exam?count=5')
        if response.status_code != 200:
            print("❌ 試験ページの読み込みに失敗")
            return False
        print("✅ 試験ページ正常")
        
        # 成績ページ
        response = client.get('/scores')
        if response.status_code != 200:
            print("❌ 成績ページの読み込みに失敗")
            return False
        print("✅ 成績ページ正常")
        
        # API
        response = client.get('/api/questions?count=3')
        if response.status_code != 200:
            print("❌ API呼び出しに失敗")
            return False
        
        data = response.get_json()
        if len(data) != 3:
            print("❌ APIが正しい数の問題を返していません")
            return False
        print("✅ API正常")
    
    print("🎉 すべてのテストが成功しました！")
    print("\n📱 アプリケーションの起動方法:")
    print("   python3 app.py")
    print("   ブラウザで http://localhost:8081 にアクセス")
    
    return True

if __name__ == '__main__':
    test_app()