from pstats import Stats
from get_module import get_info
import data as d

def get_base_pokemon(pkmn_name):
    pkmn_base = get_info(f'https://pokeapi.co/api/v2/pokemon/{pkmn_name}')

    #id y peso
    pkmn_id = pkmn_base['id']
    pkmn_w = pkmn_base['weight']

    #stats
    base_stat = [status['base_stat'] for status in pkmn_base['stats']]
    stat_name = [status['stat']['url'] for status in pkmn_base['stats']]
    d.traducir(stat_name)

    pkmn_status = dict(zip(stat_name,base_stat))

    #sprite(imagen)
    pkmn_sprite = pkmn_base['sprites']['other']['official-artwork']['front_default']
    
    return pkmn_id, pkmn_w, pkmn_status, pkmn_sprite

if __name__ == '__main__':
    name = 'gardevoir'
    id, weight, stats, sprite = get_base_pokemon(name)

    print(f'#{id} {name}\nPeso: {weight/10} Kg.\nEstadísticas')
    for key in stats:
        print(f'{key}: {stats[key]}',end=' | ')

#un comentario
    

    