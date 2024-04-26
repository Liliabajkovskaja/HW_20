from core.api_service.django_app.controller.roles_api import DjangoRolesAPI

django_role_ctrl = DjangoRolesAPI()


def test_get_roles():
    roles = django_role_ctrl.get_roles()
    print(roles)
    assert len(roles) != 0
