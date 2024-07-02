from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from config import feedbacks_group, TOKEN, admin
from orms.crud import create_user, add_user_info
from user.keyboards import start_kb, send_cv_kb, order_cv_kb, back_kb
from user.lexicon import LEXICON
from user import fsm

router = Router()
router.message.filter(lambda msg: msg not in feedbacks_group)


@router.message(CommandStart())
async def start_func(message: Message):
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
async def order_cv_func(callback: CallbackQuery):
    await callback.message.edit_text(LEXICON["order_cv"], reply_markup=await order_cv_kb())


@router.callback_query(lambda c: c.data == "send_cv")
async def order_cv_func(callback: CallbackQuery, state: fsm.FSMContext):
    await state.set_state(fsm.Application.cv)
    await callback.message.edit_text(LEXICON["send_cv"], reply_markup=await back_kb())


@router.message(lambda message: message.photo, fsm.Application.cv)
async def send_cv_func(message: Message, state: fsm.FSMContext):
    await state.update_data(cv_photo=message.photo[-1].file_id)
    await state.update_data(user=message.from_user.id)
    data = await state.get_data()
    cv_photo = data["cv_photo"]
    info = {"cv_photo": cv_photo, "text": message.caption, "username": message.from_user.username,
            "telegram_id": message.from_user.id}
    await add_user_info(info)
    await message.answer(LEXICON["cv_sent"], reply_markup=await start_kb())
    bot = Bot(token=TOKEN)
    await bot.send_photo(chat_id=admin, photo=cv_photo, caption="Новый работник\n"
                                                                f"{data["user"]}\n"
                                                                f"{message.from_user.username}\n"
                                                                f"комментарий: {message.caption}")
    await state.clear()


@router.callback_query(lambda c: c.data == "write_feedback")
async def write_feedback_func(callback: CallbackQuery, state: fsm.FSMContext):
    await state.set_state(fsm.Feedback.feedback)
    await callback.message.edit_text(LEXICON["write_feedback"], reply_markup=await back_kb())


@router.message(fsm.Feedback.feedback)
async def write_feedback_func(message: Message, state: fsm.FSMContext):
    await state.update_data(text=message.text)
    await message.forward(chat_id=feedbacks_group)
    await message.answer(LEXICON["feedback_sent"], reply_markup=await start_kb())
    await state.clear()


@router.message()
async def errors(message: Message):
    await message.answer("error", reply_markup=await start_kb())
