from flask import Blueprint, current_app, flash, redirect
from flask_login import current_user, login_required, login_user
from flask_instagram.auth.exceptions import (
    DuplicateEmailException,
    InvalidCredentialsException,
)
from flask_instagram.auth.forms import LoginForm, SignUpForm
from flask_instagram.auth.mutations import create_user
from flask_instagram.auth.queries import authenticate_user
from flask_instagram.auth.template_helpers import (
    render_login_template,
    render_signup_template,
)

bp = Blueprint("auth", __name__)


@bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@bp.route("/login", methods=["GET"])
def login_get():
    if current_user.is_authenticated:
        return redirect("/profile")
    return render_login_template(LoginForm())


@bp.route("/login", methods=["POST"])
def login_post():
    form = LoginForm()
    if not form.validate_on_submit():
        return render_login_template(form)
    if form.email.data is None or form.password.data is None:
        return redirect("/login")
    try:
        authenticate_user(form.email.data, form.password.data)
        return redirect("/profile")
    except InvalidCredentialsException:
        flash("incorrect email or password")
        return redirect("/login")


@bp.route("/signup", methods=["GET"])
def signup_get():
    if current_user.is_authenticated:
        return redirect("/profile")
    return render_signup_template(SignUpForm())


@bp.route("/signup", methods=["POST"])
def singup_post():
    form = SignUpForm()

    if not form.validate_on_submit():
        return render_signup_template(form)
    if form.email.data is None or form.password.data is None:
        return redirect("/signup")
    try:
        user = create_user(form.email.data, form.password.data)
        login_user(user)
        return redirect("profile")
    except DuplicateEmailException:
        flash("user with this email already exists")
        return redirect("/signup")
