from flask import Flask


def create_app():
    app = Flask(__name__)
    with app.app_context():
        import flask_instagram.routes
        from flask_instagram.login import login_manager

        login_manager.init_app(app)
    return app
