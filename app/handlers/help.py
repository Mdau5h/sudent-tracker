from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from app.commands import for_admin
from app.auth import auth


help_router = Router()


@help_router.message(Command('help'))
@auth
async def help_handler(message: Message) -> None:
    await message.answer("\n".join(for_admin()))
