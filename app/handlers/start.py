from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from app.enums import StaticMessages

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(StaticMessages.HELLO_MESSAGE)


@router.message(Command('code'))
async def enter_code_handler(message: Message) -> None:
    await message.answer(StaticMessages.ENTER_CODE_MESSAGE)
