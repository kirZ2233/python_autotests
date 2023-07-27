import pytest
import requests
 
host = 'https://api.pokemonbattle.me:9104'
def test_status_code():

    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200
    print(response)
    
def test_part_of_answer():
    response_trainer = requests.get(f'{host}/trainers',params={'trainer_id':1311})
    
    assert response_trainer.json()['trainer_name']=='Жаба'
    print(response_trainer)