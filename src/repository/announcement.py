from typing import List

from sqlalchemy import select, delete, update, insert

from src.model.announcement import Announcement
from src.repository.base_repository import BaseRepository
from src.dto.announcement import AnnouncementCreate, AnnouncementUpdate, AnnouncementResponse


class AnnouncementRepository(BaseRepository):
    async def create_announcement(self, user_id: int, announcement_create: AnnouncementCreate) -> Announcement:
        stmt = insert(Announcement).values(
            name=announcement_create.name,
            description=announcement_create.description,
            user_id=user_id
        ).returning(Announcement)

        announcement = await self.session.execute(stmt)
        announcement = announcement.scalar()
        await self.session.commit()

        return announcement

    async def get_announcement_by_id(self, announcement_id: int) -> Announcement | None:
        stmt = select(Announcement).where(Announcement.id == announcement_id)

        announcement = await self.session.execute(stmt)
        announcement = announcement.scalar()

        if not announcement:
            return None

        return announcement

    async def get_announcements(self) -> List[Announcement]:
        stmt = select(Announcement)

        announcements = await self.session.execute(stmt)
        announcements = announcements.scalars()

        announcements_list = [
            announcement for announcement in announcements
        ]

        return announcements_list

    async def update_announcement_by_id(self, announcement_id: int, announcement_update: AnnouncementUpdate) -> Announcement:
        stmt = update(Announcement).where(Announcement.id == announcement_id)

        if announcement_update.name:
            stmt = stmt.values(name=announcement_update.name)

        if announcement_update.description:
            stmt = stmt.values(description=announcement_update.description)

        stmt = stmt.returning(Announcement)
        announcement = await self.session.execute(stmt)
        announcement = announcement.scalar()

        await self.session.commit()

        return announcement

    async def delete_announcement_by_id(self, announcement_id: int) -> str:
        stmt = delete(Announcement).where(Announcement.id == announcement_id)

        await self.session.execute(stmt)
        await self.session.commit()

        return f"Объявление с id = {announcement_id} было успешно удалено!"
