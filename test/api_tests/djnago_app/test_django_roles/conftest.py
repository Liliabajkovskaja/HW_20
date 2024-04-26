import pytest

from core.api_service.django_app.controller.roles_api import DjangoRolesAPI
from core.api_service.django_app.controller.users_api import DjangoUsersAPIUsers
from core.api_service.django_app.dtos.payload_role_dto import PayloadDjangoRoleDTO
from core.api_service.django_app.dtos.payload_user_dto import PayloadDjangoUserDTO
from core.api_service.django_app.dtos.response_create_roles import DjangoRoleDTO

django_role_ctrl = DjangoRolesAPI()
django_user_ctrl = DjangoUsersAPIUsers()


@pytest.fixture()
def create_read_role():
    role_data = PayloadDjangoRoleDTO.random()
    resp = django_role_ctrl.post_create_role(role_data.serialize())
    yield resp
    django_role_ctrl.post_delete_role(resp.id)


@pytest.fixture
def create_read_user_function_scope():
    user_data = PayloadDjangoUserDTO.random()
    resp = django_user_ctrl.create_user(user_data.serialize())
    yield resp


@pytest.fixture
def created_role():
    role_data = PayloadDjangoRoleDTO.random()
    response = django_role_ctrl.post_create_role(data=role_data.serialize())
    yield DjangoRoleDTO(id=response.id, name=response.name)
    django_role_ctrl.post_delete_role(response.id)
