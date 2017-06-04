import os


basedir = os.path.abspath(".")
class Config:
    SECRET_KEY = "MRSMa is cool"

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir,"data-dev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir,"data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
