from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    new_user = State()
    code = State()
