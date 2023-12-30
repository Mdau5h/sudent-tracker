from enum import Enum


class StaticMessages(str, Enum):
    HELLO_MESSAGE = "Hello again!"
    HELLO_MESSAGE_UNKNOWN = "Hi, i'm Student Tracker 🤗\nSeems like we don't know each other.\nGot access code? Type /code to pass it, so I could remember you!"
    ENTER_CODE_MESSAGE = "Enter access code:"
