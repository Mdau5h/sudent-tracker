from database.session import session
from database.models import User
from database.raw.users import (
    create_or_update_user_query,
    get_user_by_id_query
)


def get_user_by_id(user_id: int) -> None | User:
    q = get_user_by_id_query(user_id)
    with session() as s:
        r = s.execute(q).fetchone()
        if r:
            return User(*r)


def save_user(**kwargs) -> None:
    q = create_or_update_user_query(**kwargs)
    with session() as s:
        s.execute(q).fetchone()
