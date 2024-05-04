from typing import List

from fastapi import APIRouter, HTTPException, status

from src.api.dependencies.containers import news_container
from src.dto.new import NewCreate, NewUpdate, NewResponse


router = APIRouter(prefix="", tags=["Действия над новостями"])


@router.post(path="/new/{user_id}", status_code=status.HTTP_201_CREATED, response_model=NewResponse)
async def create_new(user_id: int, new_create: NewCreate):
    try:
        new: NewResponse = await news_container().create_new(user_id=user_id, new_create=new_create)

        return new
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))


@router.get(path="/new/{new_id}", status_code=status.HTTP_200_OK, response_model=NewResponse)
async def get_new(new_id: int):
    try:
        new: NewResponse = await news_container().get_new(new_id=new_id)

        return new
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))


@router.get(path="/news/{user_id}", status_code=status.HTTP_200_OK, response_model=List[NewResponse])
async def get_news(user_id: int):
    try:
        news: List[NewResponse] = await news_container().get_news(user_id=user_id)

        return news
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))


@router.put(path="/new/{new_id}", status_code=status.HTTP_200_OK, response_model=NewResponse)
async def update_new(new_id: int, new_update: NewUpdate):
    try:
        new: NewResponse = await news_container().update_new(new_id=new_id, new_update=new_update)

        return new
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))


@router.delete(path="/new/{new_id}", status_code=status.HTTP_200_OK, response_model=str)
async def delete_new(new_id: int):
    try:
        result: str = await news_container().delete_new(new_id=new_id)

        return result
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))
