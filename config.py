import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:pass@localhost/john1'

    SECRET_KEY="john"

    SECRET_KEY="qwerty"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:pass@localhost/john1'

    DEBUG= True

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")

class Config:
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


config_options={
'development':DevConfig,
"production":ProdConfig
}
