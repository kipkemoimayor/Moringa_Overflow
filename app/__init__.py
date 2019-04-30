from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
<<<<<<< HEAD
from flask_simplemde import SimpleMDE

login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'
db=SQLAlchemy()
bootstrap=Bootstrap()
simple=SimpleMDE()
=======
from flask_mail import Mail

bootstrap=Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
>>>>>>> origin/feature/authentication

def create_app(config_name):


    app=Flask(__name__)
    app.config.from_object(config_options[config_name])


<<<<<<< HEAD
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)

=======
    # App Configurations
    app.config.from_object(config_options[config_name])
>>>>>>> origin/feature/authentication

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

<<<<<<< HEAD
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')
=======
    # Register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
>>>>>>> origin/feature/authentication


    return app
