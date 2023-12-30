from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from database.ext.users import (
    get_user_by_id,
    save_user
)
from app.enums import StaticMessages

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if not get_user_by_id(message.from_user.id):
        await message.answer(StaticMessages.HELLO_MESSAGE_UNKNOWN)
    else:
        await message.answer(StaticMessages.HELLO_MESSAGE)


@router.message(Command('code'))
async def enter_code_handler(message: Message) -> None:
    user = {
        'id': message.from_user.id,
        'is_admin': True
    }
    save_user(**user)
    await message.answer(StaticMessages.ENTER_CODE_MESSAGE)
