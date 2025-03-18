from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from flask_instagram.exceptions import InvalidCredentialsException
from flask_instagram.models import User
from flask_instagram.db import db

Session = sessionmaker(db.engine, expire_on_commit=False)


def get_user_by_id(user_id: int):
    stmt = select(User).where(User.id == user_id)
    with Session.begin() as session:
        result = session.execute(stmt)
        user = result.scalar_one_or_none()
    return user


def authenticate_user(email: str, password: str):
    stmt = select(User).where(User.email == email)
    with Session.begin() as session:
        result = session.execute(stmt)
    user = result.scalar_one_or_none()
    if user is None:
        raise InvalidCredentialsException()
    if not user.check_password(password):
        raise InvalidCredentialsException()
    return user
