from flask import Flask


def create_app():
    app = Flask(__name__)
    with app.app_context():
        import flask_instagram.routes
    return app
