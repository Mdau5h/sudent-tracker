from database.query import Query


def create_student_query(
        teacher_id: int,
        student_name: str,
        paid_lessons: int,
        given_lessons: int,
        is_active: bool = True
) -> Query:
    bound_params = {
        'teacher_id': teacher_id,
        'student_name': student_name,
        'paid_lessons': paid_lessons,
        'given_lessons': given_lessons,
        'lesson_diff': paid_lessons - given_lessons,
        'is_active': is_active
    }

    query = Query(
        '''
        INSERT INTO student(
            teacher_id, 
            student_name, 
            paid_lessons, 
            given_lessons, 
            lesson_diff, 
            is_active
        )
        VALUES(
            :teacher_id, 
            :student_name, 
            :paid_lessons, 
            :given_lessons, 
            :lesson_diff, 
            :is_active
        );
        ''',
        bound_params,
    )

    return query
