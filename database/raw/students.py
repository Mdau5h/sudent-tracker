from database.query import Query


def create_student_query(
        teacher_id: int,
        student_name: str,
        paid_lessons: int = 0,
        given_lessons: int = 0,
        lesson_diff: int = 0,
        is_active: bool = True,
        comment: str = ""
) -> Query:
    bound_params = {
        'teacher_id': teacher_id,
        'student_name': student_name,
        'paid_lessons': paid_lessons,
        'given_lessons': given_lessons,
        'lesson_diff': lesson_diff,
        'is_active': is_active,
        'comment': comment
    }

    query = Query(
        '''
        INSERT INTO student(
            teacher_id, 
            student_name, 
            paid_lessons, 
            given_lessons, 
            lesson_diff, 
            is_active,
            comment
        )
        VALUES(
            :teacher_id, 
            :student_name, 
            :paid_lessons, 
            :given_lessons, 
            :lesson_diff, 
            :is_active,
            :comment
        );
        ''',
        bound_params,
    )

    return query


def update_student_query(
        id: int,
        **fields,
) -> Query:
    bound_params = {
        'id': id,
        **fields,
    }

    fields_template = ",".join((
        f"{field_name}=:{field_name}"
        for field_name in fields.keys()
    ))

    query = Query(
        f'''
        UPDATE student SET {fields_template} WHERE id=:id;
        ''',
        bound_params,
    )

    return query


def get_student_by_id_query(id_: int) -> Query:
    bound_params = {
        'id': id_
    }

    query = Query(
        '''
        SELECT 
            id, 
            teacher_id,
            student_name,
            paid_lessons,
            given_lessons,
            lesson_diff,
            is_active,
            comment
        FROM student WHERE id=:id;
        ''',
        bound_params,
    )

    return query


def get_students_by_tg_id_query(teacher_id: int) -> Query:
    bound_params = {
        'teacher_id': teacher_id
    }

    query = Query(
        '''
        SELECT 
            id, 
            teacher_id,
            student_name,
            paid_lessons,
            given_lessons,
            lesson_diff,
            is_active,
            comment
        FROM student WHERE teacher_id=:teacher_id;
        ''',
        bound_params,
    )

    return query


def delete_student_by_id_query(id_: int) -> Query:
    bound_params = {
        'id': id_
    }

    query = Query(
        '''
        DELETE FROM student WHERE id=:id;
        ''',
        bound_params,
    )

    return query
