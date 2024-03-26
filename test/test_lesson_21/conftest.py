import random

import pytest
from faker import Faker

from api_service.users.controllers.users_api import UsersAPI

faker = Faker()
user_api = UsersAPI()


@pytest.fixture
def get_new_user_body():
    return {
        "name": faker.name(),
        "email": faker.email(),
        "gender": random.choice(["male", "female"]),
        "status": random.choice(["active", "inactive"])
    }