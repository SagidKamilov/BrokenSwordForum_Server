from datetime import datetime

from pydantic import BaseModel, Field


class AnnouncementCreate(BaseModel):
    name: str
    description: str


class AnnouncementUpdate(BaseModel):
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)


class AnnouncementResponse(BaseModel):
    id: int
    name: str
    description: str
    create_at: datetime
    update_at: datetime
