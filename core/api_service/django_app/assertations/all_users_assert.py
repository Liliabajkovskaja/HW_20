from core.api_service.django_app.dtos.response_user_dto import DjangoUserDTO
from assertpy import soft_assertions, assert_that


def assert_get_all_users(resp: [DjangoUserDTO], expected_user: DjangoUserDTO):

    assert_that(len(resp), 'quantity of users more tan 0').is_not_zero()

    ids = [k.id_ for k in resp]

    with soft_assertions():
        assert_that(ids, 'Id uniques').does_not_contain_duplicates()

        user = [k for k in resp if k.id_ == expected_user.id_]
        assert_that(len(user), f'User was found {expected_user.id_}').is_equal_to(1)
        assert_user(user[0], expected_user)


def assert_user(actual_user: DjangoUserDTO, expected_user: DjangoUserDTO):

    with soft_assertions():
        assert_that(actual_user.username, 'username').is_equal_to(expected_user.username)
        assert_that(actual_user.email, 'email').is_equal_to(expected_user.email)
