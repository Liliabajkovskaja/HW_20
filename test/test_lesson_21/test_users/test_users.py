import logging

from core.api_service.users.assertations.user_aserts import UserAsserts
from utils.enums import Enviroments
from test.test_lesson_21.conftest import user_api
from core.api_service.users.dtos.payload_create_user import CreateUserPayload

import pytest
import os


logger = logging.getLogger(__file__)


def test_all_users_are_unique():

    response = user_api.get_all_users()

    ids = [k.id for k in response]
    assert len(set(ids)) == len(ids)


@pytest.mark.skipif(os.getenv('current_env') == Enviroments.DEV.value, reason='only for prod')
def test_create_user():

    payload = CreateUserPayload.random()
    response = user_api.create_user(body=payload.get_dict())
    UserAsserts.assert_created_user(payload, response)
