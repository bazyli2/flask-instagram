from datetime import datetime
from typing import List
from flask_login import UserMixin
from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from werkzeug.security import check_password_hash, generate_password_hash


class Base(DeclarativeBase):
    pass

class User(Base, UserMixin):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), index=True, unique=True)
    password_hash: Mapped[str] = mapped_column(String(256))
    photos: Mapped[List["Photo"]] = relationship(back_populates='user')

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

class Photo(Base):
    __tablename__ = "photo"
    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String(256))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped['User'] = relationship(back_populates='photos')
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
