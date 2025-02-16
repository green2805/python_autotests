import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'afa537f072099fdd16c3c5e50376991f'
HEADER = {'content-type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '22655'





def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_code200():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200