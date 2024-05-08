import os
basedir = os.path.abspath(os.path.dirname(__file__))




class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    print(SQLALCHEMY_DATABASE_URI)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    ADMINS = ['shorttime104@gmail.com']
    LANGUAGES = ['es','en', 'bn']
    POSTS_PER_PAGE = 25
    MS_TRANSLATOR_KEY = os.getenv('MS_TRANSLATOR_KEY')
    REGION = 'southeastasia'

    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'

    LOG_TO_STDOUT = os.getenv('LOG_TO_STDOUT', None)