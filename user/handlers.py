from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from config import feedbacks_group
from orms.crud import create_user
from user.keyboards import start_kb, send_cv_kb, order_cv_kb, back_kb
from user.lexicon import LEXICON
from user import fsm

router = Router()


@router.message(CommandStart())
async def start_func(message: Message):
    print(message.chat.id)
    user = {"username": message.from_user.username,
            "telegram_id": message.from_user.id}
    await create_user(user)
    await message.answer(LEXICON["start"], reply_markup=await start_kb())


@router.callback_query(lambda c: c.data == "get_job")
async def get_job_func(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON["get_job"], reply_markup=await send_cv_kb())


@router.callback_query(lambda c: c.data == "back")
async def back_func(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON["start"], reply_markup=await start_kb())


@router.callback_query(lambda c: c.data == "order_cv")
async def order_cv_func(callback: CallbackQuery, state: fsm.FSMContext):
    await state.clear()
    await callback.message.edit_text(LEXICON["order_cv"], reply_markup=await order_cv_kb())


@router.callback_query(lambda c: c.data == "send_cv")
async def order_cv_func(callback: CallbackQuery, state: fsm.FSMContext):
    await state.set_state(fsm.Application.cv)
    await callback.message.edit_text(LEXICON["send_cv"], reply_markup=await back_kb())


@router.message(lambda message: message.photo, fsm.Application.cv)
async def send_cv_func(message: Message, state: fsm.FSMContext):
    await state.update_data(cv_photo=message.photo[-1].file_id)
    await message.answer(message.photo[-1].file_id, reply_markup=await back_kb())


@router.callback_query(lambda c: c.data == "write_feedback")
async def write_feedback_func(callback: CallbackQuery, state: fsm.FSMContext):
    await state.set_state(fsm.Feedback.feedback)
    await callback.message.edit_text(LEXICON["write_feedback"], reply_markup=await back_kb())


@router.message(fsm.Feedback.feedback)
async def write_feedback_func(message: Message, state: fsm.FSMContext):
    await state.update_data(text=message.text)
    await message.forward(chat_id=feedbacks_group)
    await message.answer(LEXICON["feedback_sent"], reply_markup=await start_kb())
