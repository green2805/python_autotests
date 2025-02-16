import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'afa537f072099fdd16c3c5e50376991f'
HEADER = {'content-type': 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "german@dolnikov.ru",
    "password": "Iloveqa1"
}

new_pokemon = {
    "name": "generate",
    "photo_id": 77
}

pockemon_name = {
    "pokemon_id": "236616",
    "name": "baluzavr",
    "photo_id": 77
}

pokeball_name = {
    "pokemon_id": "236616"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = new_pokemon)
print(response_create.text)
message = response_create.json()['message']
print(message)

response_namecreate = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = pockemon_name)
print(response_namecreate.text)
message = response_namecreate.json()['message']
print(message)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = pokeball_name)
message = response_pokeball.json()['message']
print(message)

