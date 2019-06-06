import os

DB_NAME = os.getenv('DB_NAME', 'db')
DB_USER = os.getenv('DB_USER', 'test')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = os.getenv('DB_PORT', '5432')

SSO_URL = os.getenv('SSO_URL', '__DEFINE_ME__')
SOCIAL_AUTH_UNTI_KEY = os.getenv('SOCIAL_AUTH_UNTI_KEY', '__DEFINE_ME__')
SOCIAL_AUTH_UNTI_SECRET = os.getenv('SOCIAL_AUTH_UNTI_SECRET', '__DEFINE_ME__')

DEBUG = str(os.getenv('DEBUG', False)) == 'True'

if os.getenv('SECRET_KEY', None):
    SECRET_KEY = os.getenv('SECRET_KEY')

BASE_URL = os.getenv('BASE_URL', 'http://example.com')
