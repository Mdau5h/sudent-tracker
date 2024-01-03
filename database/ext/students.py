import typing as t
from database.session import session
from database.models import Student
from database.raw.students import (
    create_student_query,
    update_student_query
)


def save_student(**kwargs) -> None:
    q = create_student_query(**kwargs)
    with session() as s:
        s.execute(q).fetchone()


def update_student(**kwargs) -> None:
    q = update_student_query(**kwargs)
    with session() as s:
        s.execute(q).fetchone()
