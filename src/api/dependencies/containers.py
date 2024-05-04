from src.model.setting import AsyncDatabase

from src.service.user import UserService
from src.service.new import NewService
from src.service.announcement import AnnouncementService

from src.repository.user import UserRepository
from src.repository.new import NewRepository
from src.repository.announcement import AnnouncementRepository

from src.security.password import HashGenerator


async_database = AsyncDatabase()
async_database.initialize_engine()
async_database.initialize_session()


def user_container() -> UserService:
    async_session = async_database.get_session()
    hash_generator = HashGenerator()
    user_repository = UserRepository(async_session=async_session())
    user_service = UserService(user_repository=user_repository, hash_generator=hash_generator)

    return user_service


def news_container() -> NewService:
    async_session = async_database.get_session()
    new_repository = NewRepository(async_session=async_session())
    new_service = NewService(new_repository=new_repository)

    return new_service


def announcement_container() -> AnnouncementService:
    async_session = async_database.get_session()
    announcement_repository = AnnouncementRepository(async_session=async_session())
    announcement_service = AnnouncementService(announcement_repository=announcement_repository)

    return announcement_service
