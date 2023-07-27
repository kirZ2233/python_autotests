import requests

host = 'https://api.pokemonbattle.me:9104'
token = 'f1bd1b1a60386a2915702039672ac9e3'

reg_poke = requests.post(f'{host}/pokemons',
                         headers={'Content-Type':'application/json','trainer_token':token},
                         json={'name':'generate','photo':'generate'})
print(reg_poke.text)

rename_poke = requests.put(f'{host}/pokemons',
                          headers={'Content-Type':'application/json','trainer_token':token},
                          json={'pokemon_id':5479,
                            'name':'generate',
                            'photo':'generate'})
print(rename_poke.text)
poke_in_ball = requests.post(f'{host}/trainers/add_pokeball',
                           headers={'Content-Type':'application/json','trainer_token':token},
                             json={'pokemon_id':5479})
poke_in_ball = poke_in_ball.json()
print(poke_in_ball)
battle_poke = requests.post(f'{host}/battle',
                            headers={'Content-Type':'application/json','trainer_token':token},
                            json={
                                'attacking_pokemon':5479,
                                'defending_pokemon':5476
                            })
battle_poke = battle_poke.json()
print(battle_poke)

