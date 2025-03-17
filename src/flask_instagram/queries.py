from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from flask_instagram.models import User
from flask_instagram.db import db

Session = sessionmaker(db.engine, expire_on_commit=False)


def get_user_by_id(user_id: int):
    stmt = select(User).where(User.id == user_id)
    with Session.begin() as session:
        result = session.execute(stmt)
        user = result.scalar_one_or_none()
    return user
