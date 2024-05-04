from typing import List

from fastapi import APIRouter, HTTPException, status, Depends

from src.api.dependencies.containers import user_container
from src.dto.user import UserCreate, UserUpdate, UserResponse


router = APIRouter(prefix="/users", tags=["Действия над пользователем"])


@router.get(path="/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user(user_id: int):
    try:
        user: UserResponse = await user_container().get_user(user_id=user_id)

        return user
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))


@router.get(path="", status_code=status.HTTP_200_OK, response_model=List[UserResponse])
async def get_users():
    users: List[UserResponse] = await user_container().get_users()

    return users


@router.put(path="/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate):
    try:
        user: UserResponse = await user_container().update_user(user_id=user_id, user_update=user_update)

        return user
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))


@router.delete(path="/{user_id}", status_code=status.HTTP_200_OK, response_model=str)
async def delete_user(user_id: int):
    try:
        result: str = await user_container().delete_user(user_id=user_id)

        return result
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))
