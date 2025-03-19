from flask import render_template

from flask_instagram.profile.forms import UploadPhotoForm


def render_upload_photo_template(form: UploadPhotoForm):
    return render_template("upload_photo.html", form=form)
