from pytest import mark
from test.api_tests.djnago_app.test_django_roles.conftest import django_role_ctrl


@mark.parametrize('method', ['delete', 'put', 'path'])
def test_unexpected_method_post_roles(method):
    getattr(django_role_ctrl.api_executor, method)(url=django_role_ctrl.roles_url, expected_status_code=405)
