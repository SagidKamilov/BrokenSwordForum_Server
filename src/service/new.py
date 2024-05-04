from typing import List

from src.repository.new import NewRepository
from src.repository.user import UserRepository
from src.model.new import New
from src.model.user import User
from src.dto.new import NewCreate, NewUpdate, NewResponse


class NewService:
    def __init__(self, new_repository: NewRepository, user_repository: UserRepository):
        self.new_repository = new_repository
        self.user_repository = user_repository

    async def create_new(self, user_id: int, new_create: NewCreate) -> NewResponse:
        check_user_exist: bool = await self.check_user_exist(user_id=user_id)

        if not check_user_exist:
            raise Exception(f"Пользователь с id = `{user_id}` не был найден!")

        new: New = await self.new_repository.create_new(user_id=user_id, new_create=new_create)

        return NewResponse(
            id=new.id,
            name=new.name,
            description=new.description,
            picture=new.picture,
            create_at=new.created_at,
            update_at=new.update_at
        )

    async def get_new(self, new_id: int) -> NewResponse:
        new: New = await self.new_repository.get_new_by_id(new_id=new_id)

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

    async def get_news(self, user_id: int) -> List[NewResponse]:
        check_user_exist: bool = await self.check_user_exist(user_id=user_id)

        if not check_user_exist:
            raise Exception(f"Пользователь с id = `{user_id}` не был найден!")

        news = await self.new_repository.get_news(user_id=user_id)

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

        new: New = await self.new_repository.update_new_by_id(new_id=new_id, new_update=new_update)

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

        result: str = await self.new_repository.delete_new_by_id(new_id=new_id)

        return result

    async def check_new_exist(self, new_id: int) -> bool:
        new: New = await self.new_repository.get_new_by_id(new_id=new_id)

        if new:
            return True
        else:
            return False

    async def check_user_exist(self, user_id: int) -> bool:
        user: User = await self.user_repository.get_user_by_id(user_id=user_id)

        if user:
            return True
        else:
            return False
