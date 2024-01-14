from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from app.enums import ButtonList


init_markup = ReplyKeyboardMarkup(
start_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=ButtonList.CREATE_STUDENT_BUTTON),
            KeyboardButton(text=ButtonList.STUDENT_LIST_BUTTON)
        ]
    ],
    resize_keyboard=True
)

student_info_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Spend lesson'),
            KeyboardButton(text='➕ Add paid lessons')
        ],
        [
            KeyboardButton(text='✍️ Add or change comment'),
            KeyboardButton(text='🗑️ Delete student')
        ],
        [
            KeyboardButton(text='🔙 Go back')
        ]
    ],
    resize_keyboard=True
)
