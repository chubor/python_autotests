import requests
import json
token = '251b5efe94265ae726c1fb8cbf944965'
host = 'https://api.pokemonbattle.me:9104'
photo = 'https://dolnikov.ru/pokemons/albums/001.png'
new_photo = 'https://dolnikov.ru/pokemons/albums/101.png'
name_pokemon = 'Pikachu'
id_trainer = 1935
header = {'Content-Type' : 'application/json', 'trainer_token' : token}


#создаем покемона
create_pokemon = requests.post(f'{host}/pokemons', json={
    "name": name_pokemon,
    "photo": photo
}, headers= header)
create_pokemon_json = create_pokemon.json()

print(create_pokemon.text)


#Смена имени покемона
body_update = {
    "pokemon_id": '5944',
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/101.png"
}
answer_update = requests.put(f'{host}/pokemons', json=body_update, headers = header)
print(answer_update.text)



#Ловим покемона в покебол
pokemon_in_pokebaall = requests.post(f'{host}/trainers/add_pokeball', json= {
    "pokemon_id": "5941"}, headers= header)
print(pokemon_in_pokebaall.text)


