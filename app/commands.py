def for_admin_user() -> list[str]:
    return [
        '/create - add new student',
        '/all - see all your students',
    ]


def for_students() -> list[str]:
    return [
        "/spend - spend lesson",
        "/add - add paid lessons",
        "/comment - add or change comment",
        "/del - delete student"
    ]