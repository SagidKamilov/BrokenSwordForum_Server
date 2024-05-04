from typing import List

from src.repository.announcement import AnnouncementRepository
from src.model.announcement import Announcement
from src.dto.announcement import AnnouncementCreate, AnnouncementUpdate, AnnouncementResponse


class AnnouncementService:
    def __init__(self, announcement_repository: AnnouncementRepository):
        self.repository = announcement_repository

    async def create_announcement(self, user_id: int, announcement_create: AnnouncementCreate) -> AnnouncementResponse:
        announcement: Announcement = await self.repository.create_announcement(user_id=user_id, announcement_create=announcement_create)

        return AnnouncementResponse(
            id=announcement.id,
            name=announcement.name,
            description=announcement.description,
            create_at=announcement.created_at,
            update_at=announcement.update_at
        )

    async def get_announcement(self, announcement_id: int) -> AnnouncementResponse:
        announcement: Announcement = await self.repository.get_announcement_by_id(announcement_id=announcement_id)

        if not announcement:
            raise Exception(f"Объявление с id = `{announcement}` не найдено!")

        return AnnouncementResponse(
            id=announcement.id,
            name=announcement.name,
            description=announcement.description,
            create_at=announcement.created_at,
            update_at=announcement.update_at
        )

    async def get_announcements(self) -> List[AnnouncementResponse]:
        announcements = await self.repository.get_announcements()

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

        announcement: Announcement = await self.repository.update_announcement_by_id(announcement_id=announcement_id,
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

        result: str = await self.repository.delete_announcement_by_id(announcement_id=announcement_id)

        return result

    async def check_announcement_exist(self, announcement_id: int) -> bool:
        announcement: Announcement = await self.repository.get_announcement_by_id(announcement_id=announcement_id)

        if announcement:
            return True
        else:
            return False
