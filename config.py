import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:1234@localhost/moringa_overflow'

    SECRET_KEY="collo"

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
    DEBUG= True

class ProdConfig(Config):
    pass

class Config:
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


config_options={
'development':DevConfig,
"production":ProdConfig
}
