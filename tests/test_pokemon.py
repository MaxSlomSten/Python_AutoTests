import requests
import pytest

HOST = "https://pokemonbattle.me:9104/"
def test_status_code():
    response = requests.get(f'{HOST}trainers', params = {"trainer_id" : 3764})
    assert response.status_code == 200

def test_name_trainers():
    response_name = requests.get(f'{HOST}trainers', params = {"trainer_id" : 3764})
    assert response_name.json()["trainer_name"] == "Васька"