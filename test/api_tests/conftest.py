
import pytest

from core.api_service import CreateUserPayload
from core.api_service.users.dtos.responses.create_user_dto import UserDTO
from test.test_lesson_21.conftest import user_api


@pytest.fixture(scope='session')
def test_create_user() -> UserDTO:

    payload = CreateUserPayload.random()
    response = user_api.create_user(body=payload.get_dict())
    return response
