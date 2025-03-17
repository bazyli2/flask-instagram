from flask_sqlalchemy import SQLAlchemy

from flask_instagram.models import Base

db = SQLAlchemy(model_class=Base)
