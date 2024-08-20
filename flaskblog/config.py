import os

class Config:
    SECRET_KEY = 'a58d60242a2df445f4ba14ea70ef94eb'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp-mail.outlook.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')