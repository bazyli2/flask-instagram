from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__, static_folder="../../static/")
    from flask_instagram.config import Config

    app.config.from_object(Config)

    with app.app_context():
        from flask_instagram.db import db

        db.init_app(app)
        Migrate(app, db)
        from flask_instagram.auth.routes import bp as auth_bp
        from flask_instagram.profile.routes import bp as profile_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(profile_bp)
        from flask_instagram.login import login_manager

        login_manager.init_app(app)
    return app
