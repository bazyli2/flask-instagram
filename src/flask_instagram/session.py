from sqlalchemy.orm import sessionmaker

from flask_instagram.db import db


Session = sessionmaker(db.engine, expire_on_commit=False)
