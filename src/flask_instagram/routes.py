from flask import current_app, redirect, render_template
from flask_login import login_required, login_user
from flask_instagram.exceptions import DuplicateEmailException
from flask_instagram.forms import LoginForm, SignUpForm
from flask_instagram.mutations import create_user
from flask_instagram.queries import authenticate_user


@current_app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@current_app.route("/profile")
@login_required
def profile():
    return "<p>Profile</p>"


@current_app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html", form=LoginForm())


@current_app.route("/login", methods=["POST"])
def login_post():
    form = LoginForm()
    if not form.validate_on_submit():
        return redirect("/login")
    if form.email.data is None or form.password.data is None:
        return redirect("/login")
    if authenticate_user(form.email.data, form.password.data) is None:
        return redirect("/login")
    else:
        return redirect("/profile")


@current_app.route("/signup", methods=["GET"])
def signup_get():
    return render_template("signup.html", form=SignUpForm())


@current_app.route("/signup", methods=["POST"])
def singup_post():
    form = SignUpForm()

    if not form.validate_on_submit():
        return redirect("/signup")
    if form.email.data is None or form.password.data is None:
        return redirect("/signup")
    try:
        user = create_user(form.email.data, form.password.data)
        login_user(user)
        return redirect("profile")
    except DuplicateEmailException:
        redirect("/signup")
    return redirect("/signup")
