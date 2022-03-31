#Modulo encargado de devolver un diccionario con los siguientes datos del pokemon
# id del pokemon
# peso del pokemon en gramos
# valores estadisticos del pokemon
# imagen frontal del pokemon (foto)
from get_module import get_info

def get_base_pokemon(pkmn_name):
    pkmn_base = get_info(f'https://pokeapi.co/api/v2/pokemon/{pkmn_name}')

    base = {
        'id': pkmn_base['id'],
        'peso': pkmn_base['weight'],
        'stats': [status['base_stat'] for status in pkmn_base['stats']],
        'pkmn_sprite': pkmn_base['sprites']['other']['official-artwork']['front_default']
    }

    return base

if __name__ == '__main__':
    name = 'gardevoir'
    base = get_base_pokemon(name)

    stat_name = ['PS','Ataque','Defensa','Ataque Especial','Defensa Especial','Velocidad']
    print(f"#{base['id']} {name.capitalize()}\nPeso: {base['peso']/10} Kg.\nEstadísticas")
    for nombre,valor in zip(stat_name,base['stats']):
        print(f'{nombre}: {valor}',end=' | ')

#un comentario
    

    