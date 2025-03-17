from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = StringField("password", validators=[DataRequired()])


class SignUpForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "password",
        validators=[
            DataRequired(),
            Length(8, 72),
            Regexp(r"\d", message="Password must include at least one digit"),
            Regexp(
                "[$&+,:;=?@#|'<>.^*()%!-]",
                message="Password must include at least one special character",
            ),
        ],
    )
    submit = SubmitField("Sign Up")
