from database.models import Student
from app.enums import StudentForm


def format_student_info(student: Student):
    msg = (f"Name: {student.student_name}\n"
           f"Paid lessons: {student.paid_lessons}\n"
           f"Given lessons: {student.given_lessons}\n"
           f"Lessons left: {student.lesson_diff}\n"
           f"Status: {'Active' if student.is_active else 'Inactive'}\n"
           f"{'Comment: ' + chr(34) + student.comment + chr(34) + chr(10) if student.comment else ''}"
           f"\n{StudentForm.WARNING_ONE_LESSON_MESSAGE.value if student.lesson_diff == 1 else ''}"
           )
    return msg
