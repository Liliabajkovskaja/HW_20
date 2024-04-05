from random import choice

import pytest

from core.dbs.sqlite_user_table import SqliteUsersTable


@pytest.fixture
def create_delete_user() -> dict:
    user_data = {
        "user_id": choice(range(3, 10000)),
        'name': 'Alex',
        'age': 20,
        'mail': 'Alex@mail.com',
    }

    SqliteUsersTable().create_user(**user_data)
    yield user_data
    SqliteUsersTable().delete_user_by_id(user_id=user_data['user_id'])
