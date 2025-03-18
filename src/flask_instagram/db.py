from flask_sqlalchemy import SQLAlchemy

from flask_instagram.auth.models import Base

db = SQLAlchemy(model_class=Base)
