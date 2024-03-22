import pytest
import requests

BASE_URL = "https://petstore.swagger.io/"

FIND_BY_STATUS_URL = f"{BASE_URL}v2/pet/findByStatus"


@pytest.mark.parametrize('value_status', ["available", "pending", 'sold'])
def test_get_pets_by_status(value_status):

    response = requests.get(url=FIND_BY_STATUS_URL, params={"status": value_status}, timeout=1)

    assert response.status_code == 200

    for pet in response.json():
        assert pet['status'] == value_status

