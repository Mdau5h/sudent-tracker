from enum import Enum


class StaticMessages(str, Enum):
    HELLO_MESSAGE = "Here you are again!\n"
    HELLO_MESSAGE_UNKNOWN = ("Hi, i'm Student Tracker 🤗\n"
                             "Seems like we don't know each other.\n"
                             "Got access code? Type /code to pass it, so I could remember you!\n")
    ENTER_CODE_MESSAGE = "Enter access code:\n"
    INCORRECT_CODE = "Incorrect code! Please, try again! 🙂\n"
    OUT_OF_ATTEMPTS = "Oops! 😬\nYou have reached the limit of attempts\n"
    ACCESS_GRANTED = "Hello, mister admin 😎 Type /help to see all available commands\n"
