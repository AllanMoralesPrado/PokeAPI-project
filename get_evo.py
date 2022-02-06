from get_module import get_info
from get_base_info import get_base_pokemon
from get_types import get_types_info
from get_species_info import get_species

def get_evolution(pkmn_name):
    evo_chain_url = get_info(f'https://pokeapi.co/api/v2/pokemon-species/{pkmn_name}/')['evolution_chain']['url']
    evo_chain_info = get_info(evo_chain_url)['chain']
    pkmn_evo_chain = [[],[],[]]

    #Level 1
    pkmn_evo_chain[0].append(evo_chain_info['species']['url'])

    #Level 2
    if evo_chain_info['evolves_to']:
        for i in range(0,len(evo_chain_info['evolves_to'])):
            pkmn_evo_chain[1].append(evo_chain_info['evolves_to'][i]['species']['url'])
            if evo_chain_info['evolves_to'][i]['evolves_to']:
                for j in range(0,len(evo_chain_info['evolves_to'][i]['evolves_to'])):
                    pkmn_evo_chain[2].append(evo_chain_info['evolves_to'][i]['evolves_to'][j]['species']['url'])
    
    #ID, NOMBRE, SPRITE, PRE_EVO, TIPOS
    for level in pkmn_evo_chain:
        if level:
            for index in range(len(level)):
                pkmn_nm = get_info(level[index])['name']
                base = get_base_pokemon(pkmn_nm)
                pkmn_id, pkmn_sprite = base[0], base[3]
                species = get_species(pkmn_nm)
                pkmn_pre_evo = species[0]
                types = get_types_info(pkmn_nm)
                pkmn_types, pkmn_types_en, spec_types = types[0], types[1], types[2]
                level[index] = dict(id = pkmn_id, name = pkmn_nm, sprite = pkmn_sprite, pre_evo = pkmn_pre_evo, types = pkmn_types, types_en = pkmn_types_en, spec = spec_types)
        
    return pkmn_evo_chain

if __name__ == '__main__':
    print(get_evolution('gardevoir'))