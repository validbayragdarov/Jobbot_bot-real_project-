import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN
from orms.models import create_tables
from user.handlers import router as user_router

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    """
    Запуск бота
    """
    dp.include_router(user_router)
    logging.basicConfig(level=logging.INFO)
    await create_tables()
    await dp.start_polling(bot)

asyncio.run(main())
