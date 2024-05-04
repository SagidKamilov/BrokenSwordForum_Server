from datetime import date

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    password: str
    birthday: date
    email: EmailStr


class UserUpdate(BaseModel):
    username: str | None
    password: str | None
    birthday: date | None
    email: EmailStr | None


class UserResponse(BaseModel):
    id: int
    username: str
    birthday: date
    email: EmailStr
