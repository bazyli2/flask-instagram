from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UploadPhotoForm(FlaskForm):
    photo = FileField(
        validators=[
            FileRequired(),
        ]
    )
    description = StringField("description", validators=[DataRequired()])
    submit = SubmitField("Upload")
