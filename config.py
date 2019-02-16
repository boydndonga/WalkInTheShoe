

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    CSRF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DB')


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DB')


config_options = {
    "production": ProdConfig,
    "default": DevConfig,
    "testing": TestConfig}