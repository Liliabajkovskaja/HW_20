import pytest
from core.api_service.django_app.controller.roles_api import DjangoRolesAPI
from core.api_service.django_app.dtos.payload_user_dto import PayloadDjangoUserDTO
from core.api_service.django_app.utils.validations_messages import REQUIRED_FIELD, EMPTY_FIELD

django_role_ctrl = DjangoRolesAPI()
def test_add_user_to_role(create_read_role, create_read_user_function_scope):
    role = create_read_role
    user = create_read_user_function_scope

    django_role_ctrl.post_add_user(role_id=role.id_, data={'user_id': user.id_})

    resp = django_role_ctrl.get_role_with_users(role.id_)

    assert user.id_ in resp.users
# def test_add_user_to_role_with_unexcected_id(create_read_role, create_read_user_function_scope):
#     role = create_read_role
#     user = create_read_user_function_scope
#
#     django_role_ctrl.post_add_user(role_id=role.id_, data={'user_id': user.id_})
#
#     resp = django_role_ctrl.get_role_with_users(role.id_)
#
#     assert user.id_ in resp.users



# def test_add_user_to_role_negative(user_id, expected_status_code, error_text, create_read_role):
#     # Создаем роль для теста
#     role = create_read_role
#     # Подготавливаем данные пользователя (в данном случае используется случайно сгенерированный PayloadDjangoUserDTO)
#     user_data = PayloadDjangoUserDTO.random()
#     # Переопределяем user_id, чтобы провести тест с разными значениями
#     data = {'user_id': user_id}
#     # Вызываем метод добавления пользователя в роль с предполагаемыми негативными параметрами
#     response = django_role_ctrl.post_add_user(role_id=role.id_, data=data, expected_status_code=expected_status_code)
#     # Проверяем, что ответ содержит ожидаемый текст ошибки
#     assert error_text in response.message


