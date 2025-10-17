import os

# サーバー設定
bind = f"0.0.0.0:{os.environ.get('PORT', 8080)}"
workers = 2
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 100
timeout = 30
keepalive = 2

# ログ設定
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# プロセス設定
preload_app = True
daemon = False
pidfile = None
tmp_upload_dir = None

# セキュリティ設定
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190