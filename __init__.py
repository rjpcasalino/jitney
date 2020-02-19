import os

from flask import Flask
import flask_login
from .user import User


def create_app(test_config=None):
    # create and configure jitney
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY = os.environ['APP_KEY'],
            DATABASE = os.path.join(app.instance_path, os.environ['JITNEY_DB'])
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth, index
    app.register_blueprint(index.bp)
    app.register_blueprint(auth.bp)

    login_manager = flask_login.LoginManager()

    login_manager.init_app(app)
    
    @login_manager.user_loader    
    def user_loader(email):
        user = db.query_db('SELECT email FROM users WHERE email = ?', 
        [email], one=True)
        if user is None:
            return None
        user = User()
        user.id = email
        return user
    
    return app
