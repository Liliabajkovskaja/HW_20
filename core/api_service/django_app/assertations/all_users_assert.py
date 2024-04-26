from core.api_service.django_app.controller.roles_api import DjangoRolesAPI
from core.api_service.django_app.controller.users_api import DjangoUsersAPIUsers
from core.api_service.django_app.dtos.payload_role_dto import PayloadDjangoRoleDTO
from core.api_service.django_app.dtos.response_create_roles import DjangoRoleDTO
from core.api_service.django_app.dtos.response_user_dto import DjangoUserDTO
from assertpy import soft_assertions, assert_that

django_ctrl = DjangoUsersAPIUsers()
django_role_ctrl = DjangoRolesAPI()


def assert_get_all_users(resp: [DjangoUserDTO], expected_user: DjangoUserDTO):
    assert_that(len(resp), 'quantity of users more than 0').is_not_zero()

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


def assert_user_was_created(expected_user: DjangoUserDTO, user_id: int):
    api_user = django_ctrl.get_user(user_id)
    assert_user(api_user, expected_user)


def assert_role_was_created(expected_role: PayloadDjangoRoleDTO, actual_role: PayloadDjangoRoleDTO):
    with soft_assertions():
        assert_that(actual_role.name).is_equal_to(expected_role.name)


def assert_role_by_id(expected_role: PayloadDjangoRoleDTO, role_id: int):
    api_role = django_role_ctrl.get_role_by_id(role_id)
    assert_role_was_created(expected_role, api_role)


def assert_role_was_updated(updated_role: DjangoRoleDTO, expected_role_data: PayloadDjangoRoleDTO):
    with soft_assertions():
        assert_that(updated_role.name).is_equal_to(expected_role_data.name)
