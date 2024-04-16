import pytest
from core.api_service.django_app.controller.users_api import DjangoUsersAPI
from core.api_service.django_app.dtos.payload_user_dto import PayloadDjangoUserDTO

django_ctrl = DjangoUsersAPI()


@pytest.fixture(scope='session', autouse=True)
def create_read_user():
    user_data = PayloadDjangoUserDTO.random()
    resp = django_ctrl.create_user(user_data.serialize())
    yield resp
    django_ctrl.delete_user(resp.id_)
