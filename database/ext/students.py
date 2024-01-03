import typing as t
from database.session import session
from database.models import Student
from database.raw.students import (
    create_student_query
)
from database.create import rollout


def save_student(**kwargs) -> None:
    q = create_student_query(**kwargs)
    with session() as s:
        s.execute(q).fetchone()


if __name__ == '__main__':
    rollout()
    student_data = {
        'teacher_id': 9879,
        'student_name': 'Ivan',
        'paid_lessons': 10,
        'given_lessons': 5
    }
    save_student(**student_data)
