from database.session import session
from database.query import Query

create_user_table = '''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        is_admin BOOL
    );
'''

create_students_table = '''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id INTEGER,
        student_name VARCHAR,
        paid_lessons INTEGER,
        given_lessons INTEGER,
        lesson_diff INTEGER,
        is_active BOOL,
        FOREIGN KEY (teacher_id) REFERENCES users(id)
    );
'''


def rollout():
    with session() as s:
        s.execute(Query(create_students_table))
        s.execute(Query(create_user_table))
