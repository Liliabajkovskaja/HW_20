from core.api_service.django_app.assertations.all_users_assert import assert_get_all_users
from ..conftest import django_ctrl


def test_get_all_users(create_read_user):
    resp = django_ctrl.get_all_users()
    assert_get_all_users(resp, create_read_user)
