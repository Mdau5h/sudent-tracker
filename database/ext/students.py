from database.session import session
from database.models import Student
from database.raw.students import (
    create_student_query,
    update_student_query,
    get_student_by_id_query
)
from database.create import rollout


def save_student(**kwargs) -> None:
    q = create_student_query(**kwargs)
    with session() as s:
        s.execute(q).fetchone()


def update_student(id: int, **kwargs) -> None:
    q = update_student_query(id, **kwargs)
    with session() as s:
        s.execute(q).fetchone()


def get_student_by_id(student_id: int) -> None | Student:
    q = get_student_by_id_query(student_id)
    with session() as s:
        r = s.execute(q).fetchone()
        if r:
            return Student(*r)
