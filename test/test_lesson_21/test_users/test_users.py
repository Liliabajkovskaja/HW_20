import logging

from api_service.users.assertations.user_aserts import UserAsserts
from test.test_lesson_21.conftest import user_api
from api_service.users.dtos.payload_create_user import CreateUserPayload

from assertpy import assert_that, soft_assertions


logger = logging.getLogger(__file__)


def test_all_users_are_unique():

    response = user_api.get_all_users()

    ids = [k['id'] for k in response.json()]
    assert len(set(ids)) == len(ids)


def test_create_user():

    payload = CreateUserPayload.random().get_dict()
    response = user_api.create_user(body=payload)
    UserAsserts.assert_create_user_response(payload, response.json())




# def test_create_user(get_new_user_body):
#     logger.info(get_new_user_body)
#     response = user_api.create_user(body=get_new_user_body)
#
#     #  asserts
#     assert response.json().get('id') is not None, 'response has no id property'
#
#     for k in get_new_user_body:
#         assert get_new_user_body[k] == response.json()[k]
