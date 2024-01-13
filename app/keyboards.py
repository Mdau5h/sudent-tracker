from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


init_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✍️ Add new student'),
            KeyboardButton(text='📋 See list of your students')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
