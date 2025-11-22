# main.py
import json
from engine.pokemon import Pokemon
from engine.batalha import batalha
import os

DATA_PATH = os.path.join("data", "pokemons.json")

def carregar_pokemons_do_json(caminho=DATA_PATH):
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    lista = []
    for p in dados:
        lista.append(Pokemon.from_dict(p))
    return lista

if __name__ == "__main__":
    pokemons = carregar_pokemons_do_json()
    if len(pokemons) < 2:
        print("Coloque pelo menos 2 pokemons em data/pokemons.json")
        exit(1)

    # escolhe os dois primeiros (muda aqui se quiser escolher por nome)
    p1 = pokemons[0]
    p2 = pokemons[1]

    vencedor = batalha(p1, p2)
    print("Fim da simulação. Vencedor:", vencedor.nome)
