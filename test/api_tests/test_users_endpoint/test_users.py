import logging

from api_service.users.assertations.user_aserts import UserAsserts
from api_service.users.dtos.payload_create_user import CreateUserPayload
from test.test_lesson_21.conftest import user_api

logger = logging.getLogger(__file__)


def test_all_users_are_unique():

    response = user_api.get_all_users()

    ids = [k.id for k in response]
    assert len(set(ids)) == len(ids)


def test_create_user():

    payload = CreateUserPayload.random()
    response = user_api.create_user(body=payload.get_dict())

    UserAsserts.assert_created_user(payload, response)


def test_get_user_is_the_same_as_in_get_all_users():

    response = user_api.get_all_users()
    user = response[0]
    response = user_api.get_user(user_id=user.id)

    UserAsserts.assert_created_user(user, response)

