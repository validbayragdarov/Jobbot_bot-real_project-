from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import feedbacks

# ================================= START KB ==================================
back_btn = InlineKeyboardButton(text="⬅️ Назад", callback_data="back")


async def back_kb():
    return InlineKeyboardMarkup(inline_keyboard=[[back_btn]])


async def order_cv_kb():
    write_us = InlineKeyboardButton(text='👤 Написать нам', url="https://t.me/validba")
    return InlineKeyboardMarkup(inline_keyboard=[[back_btn, write_us]])


async def send_cv_kb():
    order_cv = InlineKeyboardButton(text="📄 Заказать CV", callback_data="order_cv")
    send_cv = InlineKeyboardButton(text="📄 Отправить CV", callback_data="send_cv")
    new_cv = InlineKeyboardButton(text="Создать CV", url="https://europass.europa.eu/en")

    return InlineKeyboardMarkup(inline_keyboard=[[send_cv, order_cv], [new_cv], [back_btn]])


async def start_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='💼 Устроиться на работу', callback_data='get_job'),
    ],
        [InlineKeyboardButton(text='💬 Отзывы', url=feedbacks),
         InlineKeyboardButton(text='📝 Оставить отзыв', callback_data="write_feedback")],
        [InlineKeyboardButton(text='👤 Написать нам', url="https://t.me/validba")]
    ])
    return kb
