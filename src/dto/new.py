from datetime import datetime

from pydantic import BaseModel, Field


class NewCreate(BaseModel):
    name: str
    description: str
    picture: str


class NewUpdate(BaseModel):
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    picture: str | None = Field(default=None)


class NewResponse(BaseModel):
    id: int
    name: str
    description: str
    picture: str
    create_at: datetime
    update_at: datetime
