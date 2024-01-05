from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from re import match
from app.states import (
    CreateStudentStates,
    GetStudentStates
)
from app.enums import (
    CreateStudentForm,
    GetStudentForm
)
from database.ext.students import (
    save_student,
    get_student_by_id,
    get_students_by_tg_id
)
from app.utils import (
    format_student_list,
    format_student_info
)
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
    if not match("^\\d+$", message.text):
        await message.answer(CreateStudentForm.INCORRECT_INPUT_MESSAGE)
    else:
        await state.update_data(paid_lessons=int(message.text))
        await state.set_state(CreateStudentStates.given_lessons)
        await message.answer(CreateStudentForm.ENTER_GIVEN_MESSAGE)


@students_router.message(CreateStudentStates.given_lessons)
@auth
async def enter_given_lessons(message: Message, state: FSMContext) -> None:
    if not match("^\\d+$", message.text):
        await message.answer(CreateStudentForm.INCORRECT_INPUT_MESSAGE)
    else:
        await state.update_data(given_lessons=int(message.text))
        data = await state.get_data()
        data['teacher_id'] = message.from_user.id
        data['lesson_diff'] = data['paid_lessons'] - data['given_lessons']
        save_student(**data)
        await state.clear()
        await message.answer(CreateStudentForm.ENTER_COMPLETE_MESSAGE)


@students_router.message(Command('all'))
@auth
async def get_all_students_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(GetStudentStates.choose_student)
    students = get_students_by_tg_id(message.from_user.id)
    await message.answer(GetStudentForm.LIST_MESSAGE + format_student_list(students))


@students_router.message(GetStudentStates.choose_student, F.text.startswith('/ID_'))
@auth
async def get_student_info(message: Message, state: FSMContext) -> None:
    await state.set_state(GetStudentStates.selected)
    student = get_student_by_id(int(message.text[4:]))
    await message.answer(format_student_info(student))
