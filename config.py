class Config:
    pass

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
