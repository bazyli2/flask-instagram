from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from flask_instagram.db import db
from flask_instagram.exceptions import DuplicateEmailException
from flask_instagram.models import User


Session = sessionmaker(db.engine, expire_on_commit=False)


def create_user(email: str, password: str):
    stmt = select(User).where(User.email == email)
    with Session.begin() as session:
        existing_user = session.execute(stmt).scalar_one_or_none()
        if existing_user is not None:
            raise DuplicateEmailException
        user = User(email=email)
        user.set_password(password)
    return user
