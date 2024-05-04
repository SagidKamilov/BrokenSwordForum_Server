from fastapi import APIRouter, HTTPException, status

from src.api.dependencies import user_container
from src.dto.user import UserCreate, UserUpdate, UserResponse


router = APIRouter(prefix="/users", tags=["Действия над пользователем"])


@router.post(path="", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user_create: UserCreate):
    user: UserResponse = await user_container().create_user(user_create=user_create)

    return user
