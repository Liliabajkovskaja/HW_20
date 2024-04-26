from core.api_service.django_app.assertations.all_users_assert import assert_role_was_updated
from core.api_service.django_app.dtos.payload_role_dto import PayloadDjangoRoleDTO
from test.api_tests.djnago_app.test_django_roles.conftest import django_role_ctrl


def test_put_role_by_id(create_read_role):
    role_data = create_read_role
    updated_role_data = PayloadDjangoRoleDTO.random()
    updated_role = django_role_ctrl.put_role_by_id(role_data.id, data=updated_role_data.serialize())
    assert_role_was_updated(updated_role, updated_role_data)
