import asyncio

from orms.models import session_factory, UserData, create_tables
from sqlalchemy import select, delete, update


async def create_user(userr: dict):
    async with session_factory() as session:
        try:
            new_user = UserData(**userr)
            session.add(new_user)
            await session.flush()
            await session.commit()
        except Exception as ex:
            raise ex


user = {"id": 1, "telegram_id": 135431654}


async def main():
    await create_tables()
    await create_user(user)


asyncio.run(main())
