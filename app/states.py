from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    new_user = State()
    code = State()


class CreateStudentStates(StatesGroup):
    name = State()
    paid_lessons = State()
    given_lessons = State()


class GetStudentStates(StatesGroup):
    choose_student = State()
    selected = State()
    add_lessons = State()
    add_comment = State()
    del_confirm = State()
