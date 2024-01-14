from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from app.enums import CommandsList
from app.keyboards import start_markup
from app.auth import auth


help_router = Router()


@help_router.message(Command('help'))
@auth
# todo: get rid of it
async def help_handler(message: Message) -> None:
    await message.answer(CommandsList.FOR_ADMIN_USER, reply_markup=start_markup)
