from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.enums import ButtonList, StaticMessages
from app.states import CreateStudentStates, GetStudentStates
from app.keyboards import start_markup, student_info_markup

cancel_router = Router()


@cancel_router.message(CreateStudentStates.name, F.text == ButtonList.CANCEL_BUTTON)
@cancel_router.message(CreateStudentStates.paid_lessons, F.text == ButtonList.CANCEL_BUTTON)
@cancel_router.message(CreateStudentStates.given_lessons, F.text == ButtonList.CANCEL_BUTTON)
async def cancel_creation_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer(StaticMessages.CANCELED_MESSAGE, reply_markup=start_markup)


@cancel_router.message(GetStudentStates.add_lessons, F.text == ButtonList.CANCEL_BUTTON)
@cancel_router.message(GetStudentStates.add_comment, F.text == ButtonList.CANCEL_BUTTON)
async def cancel_change_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.set_state(GetStudentStates.selected)
    await message.answer(StaticMessages.CANCELED_MESSAGE, reply_markup=student_info_markup)