from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_instagram.models import Base


class Photo(Base):
    __tablename__ = "photo"
    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String(256))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
