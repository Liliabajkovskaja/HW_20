import requests
import json


# FILMS_URL = "https://swapi.dev/api/films/1/?some_name=value,value2" #  params={'some_name': 'value, value2'}
# FILMS_URL = "https://swapi.dev/api/films/1/?some_name=value,some_name=value2" #  params=[('some_name', 'value'), ('some_name', 'value2')]
FILMS_URL = "https://swapi.dev/api/films/1/"


def test_get_film():

    response = requests.get(url=FILMS_URL)

    assert response.status_code == 200

    for planet_url in response.json()['planets']:

        assert requests.get(url=planet_url).status_code == 200
