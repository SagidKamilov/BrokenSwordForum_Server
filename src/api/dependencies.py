from src.model.setting import AsyncDatabase

from src.service.user import UserService

from src.repository.user import UserRepository

from src.security.password import HashGenerator


async_database = AsyncDatabase()
async_database.initialize_engine()
async_database.initialize_session()

async_session = async_database.get_session()


def user_container() -> UserService:
    hash_generator = HashGenerator()
    user_repository = UserRepository(async_session=async_session())
    user_service = UserService(user_repository=user_repository, hash_generator=hash_generator)

    return user_service
