from database.session import session
from database.query import Query

create_user_table = '''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        student_name VARCHAR,
        paid_lessons_count INTEGER,
        given_lesson_count INTEGER,
        lesson_diff INTEGER,
        is_active BOOL
    );
'''


def rollout():
    with session() as s:
        s.execute(Query(create_user_table))
