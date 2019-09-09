# config file
# where configuration of the applications is done

# system libraries
import sys
import os


class Config:
    DDEBUG = False
    SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATA_BASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


app_configuration = {
    'production': ProductionConfig,
    'testing': TestingConfig,
    'development': DevelopmentConfig
}

AppConfig = TestingConfig if 'pytest' in sys.modules else app_configuration.get(
    os.getenv('FLASK_ENV'), 'development')
