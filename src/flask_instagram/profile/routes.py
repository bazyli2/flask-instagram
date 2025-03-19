import os
from flask import Blueprint, current_app, redirect
from flask_login import login_required
from werkzeug.utils import secure_filename

from flask_instagram.profile.forms import UploadPhotoForm
from flask_instagram.profile.template_helpers import render_upload_photo_template


bp = Blueprint("profile", __name__, template_folder="templates")


@bp.route("/profile")
@login_required
def profile():
    return "<p>Profile</p>"


@bp.route("/profile/upload_photo", methods=["GET"])
@login_required
def upload_photo_get():
    return render_upload_photo_template(UploadPhotoForm())


@bp.route("/profile/upload_photo", methods=["POST"])
@login_required
def upload_photo_post():
    form = UploadPhotoForm()
    print(form.photo.)
    if not form.validate_on_submit():
        return render_upload_photo_template(form)
    if form.photo.data is None or form.description.data is None:
        return redirect("/login")
    f = form.photo.data
    filename = secure_filename(f.filename)
    if current_app.static_folder is None:
        return redirect("/profile")
    f.save(os.path.join(current_app.static_folder, filename))
    return redirect("/profile")
