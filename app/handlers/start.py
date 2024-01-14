from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from database.ext.users import (
    get_user_by_id,
    save_user
)
from app.enums import (
    StaticMessages,
    EnterCodeForm,
    ButtonList
)
from app.states import UserStates
from app.keyboards import start_markup, enter_code_markup
from app.config import config

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext) -> None:
    user_authorised = get_user_by_id(message.from_user.id)
    if not user_authorised:
        await state.set_state(UserStates.new_user)
        await message.answer(StaticMessages.HELLO_UNKNOWN_MESSAGE, reply_markup=enter_code_markup)
    else:
        # todo: adapt keyboard to non-admin user
        msg = StaticMessages.HELLO_MESSAGE
        if user_authorised.is_admin:
            msg += StaticMessages.ACCESS_GRANTED_MESSAGE
        await message.answer(msg, reply_markup=start_markup)


@start_router.message(F.text == ButtonList.ENTER_CODE_BUTTON, UserStates.new_user)
async def enter_code_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(UserStates.code)
    await state.update_data(attempts=config.CODE_ATTEMPTS)
    await message.answer(EnterCodeForm.ENTER_CODE_MESSAGE, reply_markup=ReplyKeyboardRemove())


@start_router.message(UserStates.code, F.text.casefold() == config.ACCESS_CODE)
async def process_code(message: Message, state: FSMContext):
    user = {
        'id': message.from_user.id,
        'is_admin': True
    }
    save_user(**user)
    await state.clear()
    await message.answer(StaticMessages.ACCESS_GRANTED_MESSAGE, reply_markup=start_markup)


@start_router.message(UserStates.code)
async def process_code_incorrect(message: Message, state: FSMContext):
    state_data = await state.get_data()
    await state.update_data(attempts=state_data['attempts'] - 1)
    if await state.get_data() != {'attempts': 0}:
        await message.answer(EnterCodeForm.INCORRECT_CODE_MESSAGE)
    else:
        await message.answer(EnterCodeForm.OUT_OF_ATTEMPTS_MESSAGE, reply_markup=enter_code_markup)
        await state.set_state(UserStates.new_user)
