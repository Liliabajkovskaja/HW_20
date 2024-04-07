import pytest
import allure

from core.api_service.users.dtos.payload_create_user import CreateUserPayload
from test.test_lesson_21.conftest import user_api
from utils.enums import AuthTokenInvalid


@allure.title("negative test")
@pytest.mark.api_tests
@pytest.mark.parametrize('token', list(AuthTokenInvalid))
def test_create_user_invalid_token(token):
    payload = CreateUserPayload.random().get_dict()
    user_api.create_user(body=payload, headers={'Authorization': token.value},
                         expected_status_code=401,
                         use_default_token=False)
