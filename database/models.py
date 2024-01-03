from dataclasses import dataclass


@dataclass
class User:
    id: int
    is_admin: bool


@dataclass
class Student:
    id: int
    teacher_id: int
    student_name: str
    paid_lessons: int
    given_lessons: int
    is_active: bool
