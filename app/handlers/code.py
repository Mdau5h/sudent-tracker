from aiogram.types import Message
from app.handlers.start import dp
from app.enums import StaticMessages


@dp.message(commands=['code'])
async def command_start_handler(message: Message) -> None:
    await message.answer(StaticMessages.ENTER_CODE_MESSAGE)
