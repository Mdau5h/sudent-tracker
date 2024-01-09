from enum import Enum
from app.commands import (
    for_admin_user,
    for_students
)


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
    INCORRECT_INPUT_MESSAGE = "Sorry, I didn't get you. Throw me the number, please 🙂\n"


class GetStudentForm(str, Enum):
    LIST_MESSAGE = ("Here's the list of all your students.\n"
                    "Click on their ID on the left to see more info 😉\n")
    EMPTY_LIST_MESSAGE = ("Seems like you haven't added any students.\n"
                          "Not a big deal! Let's create one with command /create\n")
    STUDENT_UPDATED_MESSAGE = "Great! Here's the updated student info:\n"


class CommandsList(str, Enum):
    FOR_ADMIN_USER = "\n".join(for_admin_user())
    FOR_STUDENTS = "\n".join(for_students())
