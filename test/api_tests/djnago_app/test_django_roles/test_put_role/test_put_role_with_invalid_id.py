import pytest
from test.api_tests.djnago_app.test_django_roles.conftest import django_role_ctrl

from core.api_service.django_app.dtos.payload_role_dto import PayloadDjangoRoleDTO


@pytest.mark.parametrize('invalid_role_id', [None, False, 99999999999, " "])
def test_put_role_with_invalid_id(invalid_role_id):
    updated_role_data = PayloadDjangoRoleDTO.random()

    with pytest.raises(AssertionError):
        response = django_role_ctrl.put_role_by_id(invalid_role_id, data=updated_role_data.serialize())
        assert response.status_code == 404
