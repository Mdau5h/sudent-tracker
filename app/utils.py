from database.models import Student


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
           f"Status: {'Active' if student.is_active else 'Inactive'}\n")
    return msg
