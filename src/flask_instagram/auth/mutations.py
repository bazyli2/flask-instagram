from sqlalchemy import select
from flask_instagram.auth.exceptions import DuplicateEmailException
from flask_instagram.auth.models import User
from flask_instagram.session import Session


def create_user(email: str, password: str):
    stmt = select(User).where(User.email == email)
    with Session.begin() as session:
        existing_user = session.execute(stmt).scalar_one_or_none()
        if existing_user is not None:
            raise DuplicateEmailException
        user = User(email=email)
        user.set_password(password)
        session.add(user)
    return user
