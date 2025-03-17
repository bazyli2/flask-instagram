from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    from flask_instagram.config import Config

    app.config.from_object(Config)

    with app.app_context():
        from flask_instagram.db import db

        db.init_app(app)
        migrate = Migrate(app, db)
        import flask_instagram.routes
        from flask_instagram.login import login_manager

        login_manager.init_app(app)
    return app
