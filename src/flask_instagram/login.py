import flask_login

login_manager = flask_login.LoginManager()

login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    from flask_instagram.queries import get_user_by_id

    return get_user_by_id(int(user_id))
