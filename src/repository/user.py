from sqlalchemy import select, delete, update, insert

from src.model.user import User
from src.repository.base_repository import BaseRepository
from src.dto.user import UserCreate


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
