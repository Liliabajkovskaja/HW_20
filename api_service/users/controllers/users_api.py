import json

from api_service.base_api import BaseApi


class UsersAPI:

    api_executor = BaseApi()
    base_url = "https://gorest.co.in"
    all_users_url = f"{base_url}/public/v2/users"

    token = {'Authorization': 'Bearer 3242477d83cfc80363eb54ba6d030a851202f93fedaa3c05ae2ecc0449b2831d'}

    def get_all_users(self):

        return self.api_executor.get(url=self.all_users_url, expected_status_code=200)

    def create_user(self, body: dict, headers=None, use_default_token=True):

        if headers and use_default_token:
            headers.update(self.token)

        return self.api_executor.post(
            url=self.all_users_url,
            headers=headers or self.token,
            body=body,
            expected_status_code=201
        )
