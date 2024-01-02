from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database.ext.users import (
    get_user_by_id,
    save_user
)
from app.enums import StaticMessages
from app.states import UserStates
from app.config import config

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    user_authorised = get_user_by_id(message.from_user.id)
    if not user_authorised:
        await state.set_state(UserStates.new_user)
        await message.answer(StaticMessages.HELLO_MESSAGE_UNKNOWN)
    else:
        msg = StaticMessages.HELLO_MESSAGE
        if user_authorised.is_admin:
            msg += StaticMessages.ACCESS_GRANTED
        await message.answer(msg)


@router.message(UserStates.new_user, Command('code'))
async def enter_code_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(UserStates.code)
    await message.answer(StaticMessages.ENTER_CODE_MESSAGE)


@router.message(UserStates.code, F.text.casefold() == config.ACCESS_CODE)
async def process_code(message: Message, state: FSMContext):
    user = {
        'id': message.from_user.id,
        'is_admin': True
    }
    save_user(**user)
    await state.clear()
    await message.answer(StaticMessages.ACCESS_GRANTED)


@router.message(UserStates.code)
async def process_code_incorrect(message: Message):
    await message.answer(StaticMessages.INCORRECT_CODE)
