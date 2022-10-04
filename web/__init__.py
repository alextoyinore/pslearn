from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'starbase.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db)

    from .auth import auth
    from .views import view
    from .models import User, Course, CourseCategory

    app.register_blueprint(auth)
    app.register_blueprint(view)

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('web/' + DB_NAME):
        db.create_all(app=app)
        print(f'Database {DB_NAME} successfully create.')

