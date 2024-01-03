from enum import Enum


class StaticMessages(str, Enum):
    HELLO_MESSAGE = "Here you are again!\n"
    HELLO_UNKNOWN_MESSAGE = ("Hi, i'm Student Tracker 🤗\n"
                             "Seems like we don't know each other.\n"
                             "Got access code? Type /code to pass it, so I could remember you!\n")
    HELP_MESSAGE = "You shouldn't see this if you are not authorised\n"
    ACCESS_GRANTED_MESSAGE = "Hello, mister admin 😎 Type /help to see all available commands\n"


class EnterCodeForm(str, Enum):
    ENTER_CODE_MESSAGE = "Enter access code:\n"
    INCORRECT_CODE_MESSAGE = "Incorrect code! Please, try again! 🙂\n"
    OUT_OF_ATTEMPTS_MESSAGE = "Oops! 😬\nYou have reached the limit of attempts\n"


class CreateStudentForm(str, Enum):
    pass
