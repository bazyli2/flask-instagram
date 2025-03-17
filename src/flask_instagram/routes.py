from flask import current_app, redirect, render_template
from flask_login import login_required
from flask_instagram.forms import LoginForm
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
