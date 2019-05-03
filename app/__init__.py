from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from flask_uploads import UploadSet,configure_uploads,IMAGES

login_manager=LoginManager()

db=SQLAlchemy()
bootstrap=Bootstrap()
simple=SimpleMDE()
login_manager = LoginManager()
mail = Mail()
photos = UploadSet('photos',IMAGES)


def create_app(config_name):


    app=Flask(__name__)
    app.config.from_object(config_options[config_name])
    login_manager.session_protection="strong"
    login_manager.login_view="auth.login"
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)
    mail.init_app(app)

    # configure UploadSet
    configure_uploads(app,photos)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # Register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')


    return app
