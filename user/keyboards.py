from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# ================================= START KB ==================================

async def start_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Оставить резюме', callback_data='add_application'),
    ],
        [InlineKeyboardButton(text='Посмотреть резюме', callback_data='view_application'),
         InlineKeyboardButton(text='Оставить отзыв', callback_data="write_feedback"), ]])
    return kb
