from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    new_user = State()
    code = State()


class CreateStudentStates(StatesGroup):
    name = State()
    paid_lessons = State()
    given_lessons = State()
