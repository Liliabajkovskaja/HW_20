from core.api_service.django_app.assertations.all_users_assert import assert_role_was_created
from core.api_service.django_app.controller.roles_api import DjangoRolesAPI
from core.api_service.django_app.dtos.payload_role_dto import PayloadDjangoRoleDTO

django_role_ctrl = DjangoRolesAPI()



def test_post_roles():

    role_data = PayloadDjangoRoleDTO.random()
    resp = django_role_ctrl.post_create_role(role_data.serialize())
    actual_role = django_role_ctrl.get_role_by_id(resp.id)
    assert_role_was_created(expected_role=role_data, actual_role=actual_role)




