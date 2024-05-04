from typing import List

from sqlalchemy import select, delete, update, insert

from src.model.new import New
from src.repository.base_repository import BaseRepository
from src.dto.new import NewCreate, NewUpdate, NewResponse


class NewRepository(BaseRepository):
    async def create_new(self, user_id: int, new_create: NewCreate) -> New:
        stmt = insert(New).values(
            name=new_create.name,
            description=new_create.description,
            picture=new_create.picture,
            user_id=user_id
        ).returning(New)

        new = await self.session.execute(stmt)
        new = new.scalar()
        await self.session.commit()

        return new

    async def get_new_by_id(self, new_id: int) -> New | None:
        stmt = select(New).where(New.id == new_id)

        new = await self.session.execute(stmt)
        new = new.scalar()

        if not new:
            return None

        return new

    async def get_news(self) -> List[New]:
        stmt = select(New)

        news = await self.session.execute(stmt)
        news = news.scalars()

        news_list = [
            new for new in news
        ]

        return news_list

    async def update_new_by_id(self, new_id: int, new_update: NewUpdate) -> New:
        stmt = update(New).where(New.id == new_id)

        if new_update.name:
            stmt = stmt.values(name=new_update.name)

        if new_update.description:
            stmt = stmt.values(description=new_update.description)

        if new_update.picture:
            stmt = stmt.values(picture=new_update.picture)

        stmt = stmt.returning(New)
        new = await self.session.execute(stmt)
        new = new.scalar()

        await self.session.commit()

        return new

    async def delete_new_by_id(self, new_id: int) -> str:
        stmt = delete(New).where(New.id == new_id)

        await self.session.execute(stmt)
        await self.session.commit()

        return f"Новость с id = {new_id} была успешно удалена!"
