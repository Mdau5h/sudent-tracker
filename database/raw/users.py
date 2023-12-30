from database.query import Query


def create_or_update_user_query(id: int, is_admin: bool = False) -> Query:
    bound_params = {
        'id': id,
        'is_admin': is_admin,
    }

    query = Query(
        '''
        INSERT INTO user(id, is_admin)
        VALUES(:id, :is_admin)
        ON CONFLICT(id) DO UPDATE SET is_admin=:is_admin;
        ''',
        bound_params,
    )

    return query


def get_user_by_id_query(id_: int) -> Query:
    bound_params = {
        'id': id_
    }
    query = Query(
        '''
        SELECT id, is_admin FROM user WHERE id=:id;
        ''',
        bound_params,
    )

    return query
