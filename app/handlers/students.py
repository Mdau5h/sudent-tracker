from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.states import CreateStudentStates
from app.enums import CreateStudentForm
from database.ext.students import save_student
from app.auth import auth

students_router = Router()


@students_router.message(Command('create'))
@auth
async def create_student_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(CreateStudentStates.name)
    await message.answer(CreateStudentForm.ENTER_NAME_MESSAGE)


@students_router.message(CreateStudentStates.name)
@auth
async def enter_student_name(message: Message, state: FSMContext) -> None:
    await state.update_data(student_name=message.text)
    await state.set_state(CreateStudentStates.paid_lessons)
    await message.answer(CreateStudentForm.ENTER_PAID_MESSAGE)


@students_router.message(CreateStudentStates.paid_lessons)
@auth
async def enter_paid_lessons(message: Message, state: FSMContext) -> None:
    # todo: add datatype check
    await state.update_data(paid_lessons=int(message.text))
    await state.set_state(CreateStudentStates.given_lessons)
    await message.answer(CreateStudentForm.ENTER_GIVEN_MESSAGE)


@students_router.message(CreateStudentStates.given_lessons)
@auth
async def enter_given_lessons(message: Message, state: FSMContext) -> None:
    # todo: add datatype check
    await state.update_data(given_lessons=int(message.text))
    data = await state.get_data()
    data['teacher_id'] = message.from_user.id
    data['lesson_diff'] = data['paid_lessons'] - data['given_lessons']
    save_student(**data)
    await state.clear()
    await message.answer(CreateStudentForm.ENTER_COMPLETE_MESSAGE)
