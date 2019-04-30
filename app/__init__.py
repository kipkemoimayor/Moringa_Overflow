from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE

simple = SimpleMDE()
bootstrap=Bootstrap()

def create_app(config_name):


    app=Flask(__name__)

    bootstrap.init_app(app)
    app.config.from_object(config_options[config_name])

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = "/authenticate")

    simple.init_app(app)

    return app

