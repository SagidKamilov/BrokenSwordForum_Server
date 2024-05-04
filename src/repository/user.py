from typing import List

from sqlalchemy import select, delete, update, insert

from src.model.user import User
from src.repository.base_repository import BaseRepository
from src.dto.user import UserCreate, UserUpdate


class UserRepository(BaseRepository):
    async def create_user(self, user_create: UserCreate) -> User:
        stmt = insert(User).values(
            username=user_create.username,
            hash_password=user_create.password,
            email=user_create.email,
            birthday=user_create.birthday
        ).returning(User)

        user = await self.session.execute(stmt)
        user = user.scalar()
        await self.session.commit()

        return user

    async def get_user_by_id(self, user_id: int) -> User | None:
        stmt = select(User).where(User.id == user_id)

        user = await self.session.execute(stmt)
        user = user.scalar()

        if not user:
            return None

        return user

    async def get_user_by_email(self, user_email: str) -> User | None:
        stmt = select(User).where(User.email == user_email)

        user = await self.session.execute(stmt)
        user = user.scalar()

        if not user:
            return None

        return user

    async def get_users(self) -> List[User]:
        stmt = select(User)

        users = await self.session.execute(stmt)
        users = users.scalars()

        users_list = [
            user for user in users
        ]

        return users_list

    async def update_user_by_id(self, user_id: int, user_update: UserUpdate) -> User:

        stmt = update(User).where(User.id == user_id)

        if user_update.username:
            stmt = stmt.values(username=user_update.username)

        if user_update.password:
            stmt = stmt.values(hash_password=user_update.password)

        if user_update.email:
            stmt = stmt.values(email=user_update.email)

        if user_update.birthday:
            stmt = stmt.values(birthday=user_update.birthday)

        stmt = stmt.returning(User)
        user = await self.session.execute(stmt)
        user = user.scalar()

        await self.session.commit()

        return user

    async def delete_user_by_id(self, user_id: int) -> str:
        stmt = delete(User).where(User.id == user_id)

        await self.session.execute(stmt)
        await self.session.commit()

        return f"Пользователь с id = {user_id} был успешно удален!"
