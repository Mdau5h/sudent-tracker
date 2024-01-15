from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.enums import ButtonList
from database.models import Student

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

confirm_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=ButtonList.YES_BUTTON),
            KeyboardButton(text=ButtonList.NO_BUTTON)
        ]
    ]
)


def get_students_list_markup(students: list[Student]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    [builder.button(text=f'🧑‍🎓{student.student_name}', callback_data=str(student.id)) for student in students]
    builder.adjust(1, repeat=True)
    return builder.as_markup()
