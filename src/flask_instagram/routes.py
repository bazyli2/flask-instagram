from flask import current_app, render_template

from flask_instagram.forms import LoginForm


@current_app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@current_app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/")
    return render_template("login.html", form=form)
