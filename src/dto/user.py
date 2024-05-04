from datetime import date

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    username: str
    password: str
    birthday: date
    email: EmailStr


class UserUpdate(BaseModel):
    username: str | None = Field(default=None)
    password: str | None = Field(default=None)
    birthday: date | None = Field(default=None)
    email: EmailStr | None = Field(default=None)


class UserResponse(BaseModel):
    id: int
    username: str
    birthday: date
    email: EmailStr
