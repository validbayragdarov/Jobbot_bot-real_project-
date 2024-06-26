from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# ================================= START KB ==================================
back_btn = InlineKeyboardButton(text="Назад", callback_data="back")

async def back_kb():
    return InlineKeyboardMarkup(inline_keyboard=[[back_btn]])

async def start_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='💼 Устроиться на работу', callback_data='get_job'),
    ],
        [InlineKeyboardButton(text='💬 Отзывы', callback_data="link"),
         InlineKeyboardButton(text='📝 Оставить отзыв', callback_data="write_feedback")],
        [InlineKeyboardButton(text='👤 Написать нам', callback_data="write_us")]
    ])
    return kb
