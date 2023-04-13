import requests

token = "83ba33f63672a62bf4b34562bf3d7fce"
host = "https://pokemonbattle.me:9104/"
respopnse_add = requests.post(f'{host}pokemons', headers={"trainer_token" : token}, json = {  
    "name":"Pendal",
    "photo":"https://dolnikov.ru/pokemons/albums/054.png"
})
print(respopnse_add.text)

respopnse_new_name = requests.put(f'{host}pokemons', headers={"trainer_token" : token}, json = {
    "pokemon_id": "9157",
    "name": "Васек",
    "photo": "https://dolnikov.ru/pokemons/albums/054.png"
})
print(respopnse_new_name.text)

response_add_pokeball = requests.post(f'{host}trainers/add_pokeball', headers={"trainer_token" : token}, json = {
    "pokemon_id": "9157"
})
print(response_add_pokeball.text)