from datetime import datetime

import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import functions

from src.model.base import Base


class Announcement(Base):
    __tablename__ = "announcement_bs"

    id: Mapped[int] = mapped_column(name="announcement_id", primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(name="name", type_=sqlalchemy.String(100), nullable=False)
    description: Mapped[str] = mapped_column(name="description", type_=sqlalchemy.Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(name="created_at", type_=sqlalchemy.DateTime(timezone=True), server_default=functions.now())
    update_at: Mapped[datetime] = mapped_column(name="update_at", type_=sqlalchemy.DateTime(timezone=True),
                                                server_default=functions.now(), onupdate=datetime.now())
    user_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey("user_bs.user_id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship(back_populates="announcements")
