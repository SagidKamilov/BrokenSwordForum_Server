from typing import List

from src.repository.new import NewRepository
from src.model.new import New
from src.dto.new import NewCreate, NewUpdate, NewResponse


class NewService:
    def __init__(self, new_repository: NewRepository):
        self.repository = new_repository

    async def create_new(self, user_id: int, new_create: NewCreate) -> NewResponse:
        new: New = await self.repository.create_new(user_id=user_id, new_create=new_create)

        return NewResponse(
            id=new.id,
            name=new.name,
            description=new.description,
            picture=new.picture,
            create_at=new.created_at,
            update_at=new.update_at
        )

    async def get_new(self, new_id: int) -> NewResponse:
        new: New = await self.repository.get_new_by_id(new_id=new_id)

        if not new:
            raise Exception(f"Новость с id = `{new_id}` не найдена!")

        return NewResponse(
            id=new.id,
            name=new.name,
            description=new.description,
            picture=new.picture,
            create_at=new.created_at,
            update_at=new.update_at
        )

    async def get_news(self) -> List[NewResponse]:
        news = await self.repository.get_news()

        news_response_list = [
            NewResponse(
                id=new.id,
                name=new.name,
                description=new.description,
                picture=new.picture,
                create_at=new.created_at,
                update_at=new.update_at
            )
            for new
            in news
        ]

        return news_response_list

    async def update_new(self, new_id: int, new_update: NewUpdate) -> NewResponse:
        check_new_exist: bool = await self.check_new_exist(new_id=new_id)

        if not check_new_exist:
            raise Exception(f"Новость с id = `{new_id}` не найдена!")

        new: New = await self.repository.update_new_by_id(new_id=new_id, new_update=new_update)

        return NewResponse(
            id=new.id,
            name=new.name,
            description=new.description,
            picture=new.picture,
            create_at=new.created_at,
            update_at=new.update_at
        )

    async def delete_new(self, new_id: int) -> str:
        check_new_exist: bool = await self.check_new_exist(new_id=new_id)

        if not check_new_exist:
            raise Exception(f"Новость с id = `{new_id}` не найдена!")

        result: str = await self.repository.delete_new_by_id(new_id=new_id)

        return result

    async def check_new_exist(self, new_id: int) -> bool:
        new: New = await self.repository.get_new_by_id(new_id=new_id)

        if new:
            return True
        else:
            return False
