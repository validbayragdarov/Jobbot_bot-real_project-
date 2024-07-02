import asyncio

from orms.models import session_factory, UserData, create_tables, UserInfo, Application
from sqlalchemy import select, delete, update


async def create_user(userr: dict):
    async with session_factory() as session:
        try:
            new_user = UserData(**userr)
            session.add(new_user)
            await session.flush()
            await session.commit()
        except Exception as ex:
            print(ex)


async def add_user_info(info):
    async with session_factory() as session:
        try:
            add_info = Application(**info)
            session.add(add_info)
            await session.flush()
            await session.commit()
        except Exception as ex:
            print(ex)
