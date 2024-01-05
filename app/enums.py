from enum import Enum
from app.commands import for_admin


class StaticMessages(str, Enum):
    HELLO_MESSAGE = "Here you are again!\n"
    HELLO_UNKNOWN_MESSAGE = ("Hi, i'm Student Tracker 🤗\n"
                             "Seems like we don't know each other.\n"
                             "Got access code? Type /code to pass it, so I could remember you!\n")
    ACCESS_GRANTED_MESSAGE = "Hello, mister admin 😎 Type /help to see all available commands\n"


class EnterCodeForm(str, Enum):
    ENTER_CODE_MESSAGE = "Enter access code:\n"
    INCORRECT_CODE_MESSAGE = "Incorrect code! Please, try again! 🙂\n"
    OUT_OF_ATTEMPTS_MESSAGE = "Oops! 😬\nYou have reached the limit of attempts\n"


class CreateStudentForm(str, Enum):
    ENTER_NAME_MESSAGE = "Enter student's name:\n"
    ENTER_PAID_MESSAGE = "Enter number of paid lessons:\n"
    ENTER_GIVEN_MESSAGE = "Enter number of given lessons:\n"
    ENTER_COMPLETE_MESSAGE = "Cool! I've saved the student's info!\n"


class CommandsList(str, Enum):
    FOR_ADMIN = "\n".join(for_admin())
