from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from user.keyboards import start_kb

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer("Привет! Я бот, который поможет тебе найти себе место для отдыха", reply_markup=await start_kb())
