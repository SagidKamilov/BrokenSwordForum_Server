from src.repository.user import UserRepository
from src.model.user import User
from src.dto.user import UserCreate, UserUpdate, UserResponse
from src.security.password import HashGenerator


class UserService:
    def __init__(self, user_repository: UserRepository, hash_generator: HashGenerator):
        self.repository = user_repository
        self.hash_generator = hash_generator

    async def create_user(self, user_create: UserCreate) -> UserResponse:

        user_create_hash_password = UserCreate(
            username=user_create.username,
            password=self.hash_generator.generate_hash_from_password(password=user_create.password),
            email=user_create.email,
            birthday=user_create.birthday
        )

        user: User = await self.repository.create_user(user_create=user_create_hash_password)

        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            birthday=user.birthday
        )
