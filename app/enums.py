from enum import Enum


class ButtonList(str, Enum):
    ENTER_CODE_BUTTON = '🔑 Enter code'
    CREATE_STUDENT_BUTTON = '👨‍🎓 Add new student'
    STUDENT_LIST_BUTTON = '📋 See list of your students'
    SPEND_LESSON_BUTTON = '✅ Spend lesson'
    ADD_LESSONS_BUTTON = '➕ Add paid lessons'
    COMMENT_BUTTON = '✍️ Add or change comment'
    DELETE_STUDENT_BUTTON = '🗑️ Delete student'
    GO_BACK_BUTTON = '🔙 Go back'
    YES_BUTTON = '✅ Yes'
    NO_BUTTON = '🚫 No'
    CANCEL_BUTTON = '🚫 Cancel'


class StaticMessages(str, Enum):
    HELLO_MESSAGE = "Here you are again!\n"
    HELLO_UNKNOWN_MESSAGE = ("Hi, i'm Student Tracker 🤗\n"
                             "Seems like we don't know each other.\n"
                             "Got access code? Hit the button below to pass it, so I could remember you!\n")
    ACCESS_GRANTED_MESSAGE = "Hello, mister admin! Glad to see you again! 😎\nHere's what you can do now:\n"
    CANCELED_MESSAGE = "Operation canceled 👀"


class EnterCodeForm(str, Enum):
    ENTER_CODE_MESSAGE = "Enter access code:\n"
    INCORRECT_CODE_MESSAGE = "Incorrect code! Please, try again! 🙂\n"
    OUT_OF_ATTEMPTS_MESSAGE = "Oops! 😬\nYou have reached the limit of attempts\n"


class StudentForm(str, Enum):
    ENTER_NAME_MESSAGE = "Enter student's name:\n"
    ENTER_PAID_MESSAGE = "Enter number of paid lessons:\n"
    ENTER_GIVEN_MESSAGE = "Enter number of given lessons:\n"
    ENTER_COMMENT_MESSAGE = "Enter the comment: \n"
    ENTER_COMPLETE_MESSAGE = ("Cool! I've saved the student's info! 👌\n"
                              "You can see them in the list by hitting:\n"
                              f'"{ButtonList.STUDENT_LIST_BUTTON.value}"\n')
    INCORRECT_INPUT_MESSAGE = "Sorry, I didn't get you. Throw me the number, please 🙂\n"
    CONFIRM_MESSAGE = "Are you sure? There's no undo! 🤔\n"
    LIST_MESSAGE = ("Here's the list of all your students 👇\n"
                    "Click on them to see more info 😉\n")
    ADDITIONAL_MESSAGE = ("Or you can add a new one! \n"
                          f'Hit the button: "{ButtonList.CREATE_STUDENT_BUTTON.value}" to do so!\n')
    EMPTY_LIST_MESSAGE = ("Seems like you don't have any students yet. 🤔\n"
                          "Not a big deal! Let's create one!\n"
                          f'Hit the button: "{ButtonList.CREATE_STUDENT_BUTTON.value}" \n'
                          )
    WARNING_ONE_LESSON_MESSAGE = "Warning! ⚠️\nThere is only one paid lesson left!"
    STUDENT_UPDATED_MESSAGE = "Great! 🤗 Here's the updated student info:\n"
    STUDENT_DELETED_MESSAGE = "Done! Student has been deleted! 👌\n"
    DELETE_CANCELED_MESSAGE = "Deletion hasn't been confirmed 🤷\n"
