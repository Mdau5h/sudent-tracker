from enum import Enum


class StaticMessages(str, Enum):
    HELLO_MESSAGE = "Here you are again!\n"
    HELLO_MESSAGE_UNKNOWN = "Hi, i'm Student Tracker 🤗\nSeems like we don't know each other.\nGot access code? Type /code to pass it, so I could remember you!\n"
    ENTER_CODE_MESSAGE = "Enter access code:\n"
    INCORRECT_CODE = "Incorrect code 🙂\n"
    ACCESS_GRANTED = "Hello, mister admin 😎 Type /help to see all available commands\n"
