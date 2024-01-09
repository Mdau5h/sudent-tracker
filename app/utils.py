from database.models import Student
from app.enums import CommandsList


def format_student_list(students: list[Student]):
    msg = '\n'.join((
        f"/ID_{student.id}: {student.student_name}"
        for student in students
    ))
    return msg


def format_student_info(student: Student):
    msg = (f"Name: {student.student_name}\n"
           f"Paid lessons: {student.paid_lessons}\n"
           f"Given lessons: {student.given_lessons}\n"
           f"Lessons left: {student.lesson_diff}\n"
           f"Status: {'Active' if student.is_active else 'Inactive'}\n"
           f"{'Comment: ' + student.comment + chr(10) if student.comment else ''}"
           + "\n" + CommandsList.FOR_STUDENTS +
           f"\n\n/all - go back"
           )
    return msg
