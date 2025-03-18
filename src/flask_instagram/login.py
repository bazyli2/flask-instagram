import flask_login

login_manager = flask_login.LoginManager()

login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id: str):
    from flask_instagram.auth.queries import get_user_by_id

    return get_user_by_id(int(user_id))
