from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Dispatcher
from app.enums import StaticMessages

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(StaticMessages.HELLO_MESSAGE)
