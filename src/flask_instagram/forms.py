from flask_wtf import FlaskForm
from wtforms import EmailField, StringField


class LoginForm(FlaskForm):
    email = EmailField("email")
