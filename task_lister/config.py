import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some_secret_key'
    IS_DEBUG = os.environ.get('TASK_LISTER_DEBUG', '').lower() in ['1', 'true', 'yes']
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') if IS_DEBUG else os.environ.get('TASK_LISTER_KOYEB_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT =  465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('EMAIL') 
    MAIL_PASSWORD = os.environ.get('EMAIL_TOKEN')
