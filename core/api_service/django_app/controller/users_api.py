from core.api_service.base_api import BaseApi
from core.api_service.django_app.dtos.payload_user_dto import PayloadDjangoUserDTO
from core.api_service.django_app.dtos.response_user_dto import DjangoUserDTO, DjangoUserSchema


class DjangoUsersAPI:

    api_executor = BaseApi()
    base_url = "http://localhost:8000/"
    users_url = f"{base_url}users/"

    def get_all_users(self) -> [DjangoUserDTO]:

        return self.api_executor.get(url=self.users_url, expected_status_code=200,
                                     schema=DjangoUserSchema(many=True))

    def get_user(self, user_id) -> DjangoUserDTO:

        return self.api_executor.get(url=self.users_url + f'{user_id}',
                                     expected_status_code=200,
                                     schema=DjangoUserSchema())

    def create_user(self, body: PayloadDjangoUserDTO, expected_status_code=201) -> DjangoUserDTO:

        return self.api_executor.post(
            url=self.users_url,
            data=body,
            expected_status_code=expected_status_code,
            schema=DjangoUserSchema()
        )

    def update_user(self, body: PayloadDjangoUserDTO, expected_status_code=201) -> DjangoUserDTO:

        return self.api_executor.put(
            url=self.users_url,
            data=body,
            expected_status_code=expected_status_code,
            schema=DjangoUserSchema()
        )

    def delete_user(self, user_id, expected_status_code=204) -> None:

        self.api_executor.delete(
            url=self.users_url + f'{user_id}/',
            expected_status_code=expected_status_code
        )
