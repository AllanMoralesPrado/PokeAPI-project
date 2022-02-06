from get_module import get_info

def get_species(pkmn_name):
    pkmn_species = get_info(f'https://pokeapi.co/api/v2/pokemon-species/{pkmn_name}/')
    
    #evolucion anterior
    pkmn_pre = ' '

    if pkmn_species['evolves_from_species'] != None:
        pkmn_pre = pkmn_species['evolves_from_species']['name']
    else:
        pkmn_pre = 'No tiene'

    #descripcion
    descripcion = None
    for i in pkmn_species['flavor_text_entries']:
        if i['language']['name'] == 'es':
            descripcion = i['flavor_text']
            break

    return pkmn_pre, descripcion

if __name__ == '__main__':
    name = 'gardevoir'
    pre_evolution, description = get_species(name)
    print(f'Evolución anterior: {pre_evolution}')
    print(f'Description: {description}')
