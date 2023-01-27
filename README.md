Django開発環境テンプレート

・django-admin startproject your_project_name
・python3 manage.py runserver
・django-admin startapp myapp
・アプリにurl.pyを追加
・サーバーで/adminにアクセスすると管理ページに行く

Database
・python3 manage.py showmigrations
・python3 manage.py makemigrations
・python3 manage.py migrate

カスタムコマンド
・myapp/management/commands/command_name.pyを作成
・python3 manage.py command_name

settings.py
・LANGUAGE_CODE = 'ja'
・TIME_ZONE = 'Asia/Tokyo'
・STATIC_ROOT = 'path/to/static'
・ALLOWED_HOSTS = ['*']
・開発環境と本番環境で読み込む.envを分岐
import os
from dotenv import load_dotenv

if os.environ.get('APP_ENV') == 'prod':
    load_dotenv('.env.prod')
else:
    load_dotenv('.env.dev')
