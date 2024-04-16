from random import choice

import pytest
from faker import Faker

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


@pytest.fixture(autouse=True, scope='session')
def create_delete_users() -> dict:

    faker = Faker()

    user_ids = []

    for k in range(choice(range(1, 11))):
        user_data = {
            "user_id": choice(range(3, 10000)),
            'name': faker.name(),
            'age': choice(range(18, 65)),
            'mail': faker.email(),
        }
        user_ids.append(user_data['user_id'])

        SqliteUsersTable().create_user(**user_data)
    yield
    for k in user_ids:
        SqliteUsersTable().delete_user_by_id(user_id=k)

