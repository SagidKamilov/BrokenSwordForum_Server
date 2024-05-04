from typing import List

from src.repository.announcement import AnnouncementRepository
from src.repository.user import UserRepository
from src.model.announcement import Announcement
from src.model.user import User
from src.dto.announcement import AnnouncementCreate, AnnouncementUpdate, AnnouncementResponse


class AnnouncementService:
    def __init__(self, announcement_repository: AnnouncementRepository, user_repository: UserRepository):
        self.announcement_repository = announcement_repository
        self.user_repository = user_repository

    async def create_announcement(self, user_id: int, announcement_create: AnnouncementCreate) -> AnnouncementResponse:
        check_user_exist: bool = await self.check_user_exist(user_id=user_id)

        if not check_user_exist:
            raise Exception(f"Пользователь с id = `{user_id}` не был найден!")

        announcement: Announcement = await self.announcement_repository.create_announcement(user_id=user_id, announcement_create=announcement_create)

        return AnnouncementResponse(
            id=announcement.id,
            name=announcement.name,
            description=announcement.description,
            create_at=announcement.created_at,
            update_at=announcement.update_at
        )

    async def get_announcement(self, announcement_id: int) -> AnnouncementResponse:
        announcement: Announcement = await self.announcement_repository.get_announcement_by_id(announcement_id=announcement_id)

        if not announcement:
            raise Exception(f"Объявление с id = `{announcement_id}` не найдено!")

        return AnnouncementResponse(
            id=announcement.id,
            name=announcement.name,
            description=announcement.description,
            create_at=announcement.created_at,
            update_at=announcement.update_at
        )

    async def get_announcements(self, user_id: int) -> List[AnnouncementResponse]:
        check_user_exist: bool = await self.check_user_exist(user_id=user_id)

        if not check_user_exist:
            raise Exception(f"Пользователь с id = `{user_id}` не был найден!")

        announcements = await self.announcement_repository.get_announcements(user_id=user_id)

        announcements_response_list = [
            AnnouncementResponse(
                id=announcement.id,
                name=announcement.name,
                description=announcement.description,
                create_at=announcement.created_at,
                update_at=announcement.update_at
            )
            for announcement
            in announcements
        ]

        return announcements_response_list

    async def update_announcement(self, announcement_id: int, announcement_update: AnnouncementUpdate) -> AnnouncementResponse:
        check_announcement_exist: bool = await self.check_announcement_exist(announcement_id=announcement_id)

        if not check_announcement_exist:
            raise Exception(f"Объявление с id = `{announcement_id}` не найдено!")

        announcement: Announcement = await self.announcement_repository.update_announcement_by_id(announcement_id=announcement_id,
                                                                                                  announcement_update=announcement_update)

        return AnnouncementResponse(
            id=announcement.id,
            name=announcement.name,
            description=announcement.description,
            create_at=announcement.created_at,
            update_at=announcement.update_at
        )

    async def delete_announcement(self, announcement_id: int) -> str:
        check_announcement_exist: bool = await self.check_announcement_exist(announcement_id=announcement_id)

        if not check_announcement_exist:
            raise Exception(f"Объявление с id = `{announcement_id}` не найдено!")

        result: str = await self.announcement_repository.delete_announcement_by_id(announcement_id=announcement_id)

        return result

    async def check_announcement_exist(self, announcement_id: int) -> bool:
        announcement: Announcement = await self.announcement_repository.get_announcement_by_id(announcement_id=announcement_id)

        if announcement:
            return True
        else:
            return False

    async def check_user_exist(self, user_id: int) -> bool:
        user: User = await self.user_repository.get_user_by_id(user_id=user_id)

        if user:
            return True
        else:
            return False
