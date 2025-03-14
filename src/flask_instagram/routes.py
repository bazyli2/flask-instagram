from flask import current_app


@current_app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
