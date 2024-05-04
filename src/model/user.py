from typing import List
from datetime import datetime, date

import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import functions

from src.model.base import Base


class User(Base):
    __tablename__ = "user_bs"

    id: Mapped[int] = mapped_column(name="user_id", primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(name="username", type_=sqlalchemy.String(255), nullable=False)
    birthday: Mapped[date] = mapped_column(name="birthday", type_=sqlalchemy.Date(), nullable=False)
    email: Mapped[str] = mapped_column(name="email", type_=sqlalchemy.String(100), unique=True, nullable=False)
    hash_password: Mapped[str] = mapped_column(name="hash_password", type_=sqlalchemy.Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(name="created_at", type_=sqlalchemy.DateTime(timezone=True), server_default=functions.now())
    update_at: Mapped[datetime] = mapped_column(name="update_at", type_=sqlalchemy.DateTime(timezone=True),
                                                server_default=functions.now(), onupdate=datetime.now())
    # announcements: Mapped[List["Announcement"]] = relationship(back_populates="user")
    # news: Mapped[List["New"]] = relationship(back_populates="user")
