from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database.ext.users import (
    get_user_by_id,
    save_user
)
from app.enums import StaticMessages, EnterCodeForm
from app.states import UserStates
from app.config import config

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext) -> None:
    user_authorised = get_user_by_id(message.from_user.id)
    if not user_authorised:
        await state.set_state(UserStates.new_user)
        await message.answer(StaticMessages.HELLO_UNKNOWN_MESSAGE)
    else:
        msg = StaticMessages.HELLO_MESSAGE
        if user_authorised.is_admin:
            msg += StaticMessages.ACCESS_GRANTED_MESSAGE
        await message.answer(msg)


@start_router.message(UserStates.new_user, Command('code'))
async def enter_code_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(UserStates.code)
    await state.update_data(attempts=config.CODE_ATTEMPTS)
    await message.answer(EnterCodeForm.ENTER_CODE_MESSAGE)


@start_router.message(UserStates.code, F.text.casefold() == config.ACCESS_CODE)
async def process_code(message: Message, state: FSMContext):
    user = {
        'id': message.from_user.id,
        'is_admin': True
    }
    save_user(**user)
    await state.clear()
    await message.answer(StaticMessages.ACCESS_GRANTED_MESSAGE)


@start_router.message(UserStates.code)
async def process_code_incorrect(message: Message, state: FSMContext):
    state_data = await state.get_data()
    await state.update_data(attempts=state_data['attempts'] - 1)
    if await state.get_data() != {'attempts': 0}:
        await message.answer(EnterCodeForm.INCORRECT_CODE_MESSAGE)
    else:
        await message.answer(EnterCodeForm.OUT_OF_ATTEMPTS_MESSAGE)
        await state.clear()
