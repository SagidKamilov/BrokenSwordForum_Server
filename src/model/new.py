from typing import List
from datetime import datetime, date

import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import functions

from src.model.base import Base


class New(Base):
    __tablename__ = "new"

    id: Mapped[int] = mapped_column(name="new_id", primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(name="name", type_=sqlalchemy.String(100), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(name="description", type_=sqlalchemy.Text(), nullable=False)
    picture: Mapped[str] = mapped_column(name="picture", type_=sqlalchemy.Text(), nullable=False)
    user_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey("user.user_id"))
    user: Mapped["User"] = relationship(back_populates="news")
