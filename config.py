import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collo:collins@localhost/moringa_overflow'

    SECRET_KEY = "collo"

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class DevConfig(Config):
    DEBUG= True

class ProdConfig(Config):
    pass


config_options={
'development':DevConfig,
"production":ProdConfig
}
