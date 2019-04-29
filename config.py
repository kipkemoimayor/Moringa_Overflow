class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collo:collins@localhost/moringa_overflow'

class DevConfig(Config):
    DEBUG= True

class ProdConfig(Config):
    pass


config_options={
'development':DevConfig,
"production":ProdConfig
}
