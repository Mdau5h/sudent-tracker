from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from app.enums import ButtonList


enter_code_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=ButtonList.ENTER_CODE_BUTTON)
        ]
    ]
)

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
            KeyboardButton(text=ButtonList.SPEND_LESSON_BUTTON),
            KeyboardButton(text=ButtonList.ADD_LESSONS_BUTTON)
        ],
        [
            KeyboardButton(text=ButtonList.COMMENT_BUTTON),
            KeyboardButton(text=ButtonList.DELETE_STUDENT_BUTTON)
        ],
        [
            KeyboardButton(text=ButtonList.GO_BACK_BUTTON)
        ]
    ],
    resize_keyboard=True
)

