from typing import List

from fastapi import APIRouter, HTTPException, status

from src.api.dependencies.containers import announcement_container
from src.dto.announcement import AnnouncementCreate, AnnouncementUpdate, AnnouncementResponse


router = APIRouter(prefix="", tags=["Действия над объявлениями"])


@router.post(path="/announcement/{user_id}", status_code=status.HTTP_201_CREATED, response_model=AnnouncementResponse)
async def create_announcement(user_id: int, announcement_create: AnnouncementCreate):
    try:
        announcement: AnnouncementResponse = await announcement_container().create_announcement(
            user_id=user_id, announcement_create=announcement_create)

        return announcement
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))


@router.get(path="/announcement/{announcement_id}", status_code=status.HTTP_200_OK, response_model=AnnouncementResponse)
async def get_announcement(announcement_id: int):
    try:
        announcement: AnnouncementResponse = await announcement_container().get_announcement(announcement_id=announcement_id)

        return announcement
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))


@router.get(path="/announcements/{user_id}", status_code=status.HTTP_200_OK, response_model=List[AnnouncementResponse])
async def get_announcements(user_id: int):
    try:
        announcements: List[AnnouncementResponse] = await announcement_container().get_announcements(user_id=user_id)

        return announcements
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))


@router.put(path="/announcement/{announcement_id}", status_code=status.HTTP_200_OK, response_model=AnnouncementResponse)
async def update_announcement(announcement_id: int, announcement_update: AnnouncementUpdate):
    try:
        announcement: AnnouncementResponse = await announcement_container().update_announcement(
            announcement_id=announcement_id, announcement_update=announcement_update)

        return announcement
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))


@router.delete(path="/announcement/{announcement_id}", status_code=status.HTTP_200_OK, response_model=str)
async def delete_announcement(announcement_id: int):
    try:
        result: str = await announcement_container().delete_announcement(announcement_id=announcement_id)

        return result
    except Exception as error_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error_detail))
