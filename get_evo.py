from get_module import get_info

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

    return pkmn_evo_chain

if __name__ == '__main__':
    print(get_evolution('gardevoir'))