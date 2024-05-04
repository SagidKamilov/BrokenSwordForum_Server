import asyncio
from src.api.dependencies import async_database
from src.model.base import Base

from src.model.user import User
from src.model.new import New
from src.model.announcement import Announcement


engine = async_database.get_engine()


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # await conn.run_sync(Base.metadata.drop_all)


asyncio.run(create_database())
