# importação dos dados json
import json

def ImportarJson():
    with open('pokemons.json') as file:
        pokemons = json.load(file)
        return pokemons