from flask import render_template
from flask_instagram.auth.forms import LoginForm, SignUpForm


def render_login_template(form: LoginForm):
    return render_template("login.html", form=form)


def render_signup_template(form: SignUpForm):
    return render_template("signup.html", form=form)
