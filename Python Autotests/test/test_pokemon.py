import requests
import pytest

id_trainer = 1935
host = 'https://api.pokemonbattle.me:9104'

#проверяем статус код 200
def test_status_code():
    response = requests.get(f'{host}/trainers', params = {'trainer_id': id_trainer})
    assert response.status_code == 200
 

#проверяем имя тренера
def test_part_of_answer():
    answer_body = requests.get(f'{host}/trainers', params = {'trainer_id' : id_trainer})
    assert answer_body.json()['trainer_name'] == 'Ash'

#содержание полей в покемоне
@pytest.mark.parametrize('key, value', [('name', 'Ash'), ('attack', '1.0'), ('trainer_id', '1935')])
def test_parts_of_answer(key, value):
    response = requests.get(f'{host}/pokemons', params = {'trainer_id': id_trainer})
    assert response.json()[1][key] == value
