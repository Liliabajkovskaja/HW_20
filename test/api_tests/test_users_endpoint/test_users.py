import logging

import pytest

from api_service.users.assertations.user_aserts import UserAsserts
from api_service.users.dtos.payload_create_user import CreateUserPayload
from test.test_lesson_21.conftest import user_api

logger = logging.getLogger(__file__)


import allure

@allure.epic("Web interface")
@allure.feature("Essential features")
@allure.story("Authentication")
@allure.title("all users are unique")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.api_tests
def test_all_users_are_unique():

    response = user_api.get_all_users()

    ids = [k.id for k in response]
    assert len(set(ids)) == len(ids)


@allure.title("create user")
@pytest.mark.api_tests
def test_create_user():

    payload = CreateUserPayload.random()
    response = user_api.create_user(body=payload.get_dict())

    UserAsserts.assert_created_user(payload, response)


@pytest.mark.api_tests
def test_get_user_is_the_same_as_in_get_all_users():

    response = user_api.get_all_users()
    user = response[0]
    response = user_api.get_user(user_id=user.id)

    UserAsserts.assert_created_user(user, response)

