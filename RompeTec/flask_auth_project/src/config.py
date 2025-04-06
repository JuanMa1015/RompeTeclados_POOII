from datetime import timedelta
class Config:
    SECRET_KEY = 'RompeRompe'
    SQLALCHEMY_DATABASE_URI = 'postgresql://Login_owner:npg_Ko6On9iyYSZp@ep-tight-haze-a5hccwic-pooler.us-east-2.aws.neon.tech/Login?sslmode=require'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'gonzalezjuanmanuel645@gmail.com'
    MAIL_PASSWORD = 'xqaa jcmf hfia jywh'
    
    MAIL_DEFAULT_SENDER = "gonzalezjuanmanuel645@gmail.com"
    
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)