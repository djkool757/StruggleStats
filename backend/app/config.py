from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
print(os.environ.get('SECRET_KEY_SSTATS'))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR.parent / 'database' / 'sstats.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET = os.environ.get('SECRET_KEY_SSTATS')
    DEBUG = True
    CORS_HEADERS = 'Content-Type'
    CORS_ORIGINS = ['http://localhost:3000']
    CORS_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
    CORS_ALLOW_CREDENTIALS = True
    CORS_EXPOSE_HEADERS = ['Content-Length', 'X-Requested-With']
    CORS_MAX_AGE = 3600
    

