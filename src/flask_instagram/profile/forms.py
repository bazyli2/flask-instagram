from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UploadPhotoForm(FlaskForm):
    photo = FileField(
        validators=[FileRequired(), FileAllowed(["jpg", "png"], "Images only!")]
    )
    description = StringField("description", validators=[DataRequired()])
    submit = SubmitField("Upload")
