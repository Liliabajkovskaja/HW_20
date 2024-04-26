from core.api_service.django_app.assertations.all_users_assert import assert_role_by_id
from core.api_service.django_app.controller.roles_api import DjangoRolesAPI

django_role_ctrl = DjangoRolesAPI()


def test_get_role_by_id(create_read_role):
    role_data = create_read_role
    assert_role_by_id(role_data, role_data.id)
