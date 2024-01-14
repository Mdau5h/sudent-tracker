from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


init_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👨‍🎓 Add new student'),
            KeyboardButton(text='📋 See list of your students')
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
