import requests

def buscar_pokemon(numero):
    """
    Busca um pokemon a partir do seu numero na pokedex.

    :param usuario: int com o numero do pokemon na pokedex.
    :return: str com o nome do pokemon.
    """
    url = f'https://pokeapi.co/api/v2/pokemon/{numero}'
    resp = requests.get(url)
    return resp.json()['forms']

if __name__ == '__main__':
    print(buscar_pokemon(1))