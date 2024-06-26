from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from user.keyboards import start_kb, back_kb
from user.lexicon import LEXICON

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(LEXICON["start"], reply_markup=await start_kb())


@router.callback_query(lambda c: c.data == "get_job")
async def get_job(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON["get_job"], reply_markup=await back_kb())


@router.callback_query(lambda c: c.data == "back")
async def back(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON["start"], reply_markup=await start_kb())
