from get_module import get_info
from data import traducir
import poke_validation as pv

def get_types_info(pkmn_name):
    pkmn_base = get_info(f'https://pokeapi.co/api/v2/pokemon/{pkmn_name}')
    resultado_ = get_info(f'https://pokeapi.co/api/v2/pokemon-species/{pkmn_name}/')

    #fortalezas/debilidades
    #Ej: Charizard es tipo fuego, volador

    pkmn_damage_rel = {
        'double_damage_from': [],
        'double_damage_to': [],
        'half_damage_from':[],
        'half_damage_to': [],
        'no_damage_from': [],
        'no_damage_to': []
    }

    #tipo/tipo especial
    pkmn_type = [tipo['type']['url'] for tipo in pkmn_base['types']]

    #Funcion que captura tipos de pokemon y los almacena en una lista
    def add_types_rel(damage_types,type_src):
        for ts in type_src:
            damage_types.append(ts['url'])

    #Iteracion: por cada tipo el cual pertenece un pokemon
    for i in pkmn_type:
        #Capturar el diccionario con que contenga la relacion de daño entre los tipos
        tipo = get_info(i)['damage_relations']
        #Para cada lista del diccionario de relaciones de daño
        for key in pkmn_damage_rel:
            #Añadir los tipos de pokemon según la relación de daño correspondiente
            add_types_rel(pkmn_damage_rel[key],tipo[key])

    #Para cada clave del diccionario de relaciones de daño
    for i in pkmn_damage_rel:
        #Eliminar redundancias de las listas asociadas a cada clave
        pkmn_damage_rel[i] = list(set(pkmn_damage_rel[i]))
        #Traducir la URL del tipo al nombre del tipo en lenguaje "es"
        traducir(pkmn_damage_rel[i])

    traducir(pkmn_type)

    if resultado_['is_baby']:
        pkmn_type.append('Bebé')
    if resultado_['is_legendary']:
        pkmn_type.append('Legendario')
    if resultado_['is_mythical']:
        pkmn_type.append('Mítico')
    
    return pkmn_type,pkmn_damage_rel

if __name__ == '__main__':
    name = 'gardevoir'
    pokemon_tipo, pkmn_buffs_n_nerfs = get_types_info(name)
    
    print(f'Pokemon: {name}')

    print('\nTIPO')
    for i in pokemon_tipo:
        print(i, end=' ')

    print('\n\nSúper efectivo contra:')
    for value in pkmn_buffs_n_nerfs['double_damage_to']:
        print(value, end=' ')

    print('\n\nDébil contra:')
    for value in pkmn_buffs_n_nerfs['double_damage_from']:
        print(value, end=' ') 

    print('\n\nResistente contra:')
    for value in pkmn_buffs_n_nerfs['half_damage_from']:
        print(value, end=' ') 

    print('\n\nPoco eficaz contra:')
    for value in pkmn_buffs_n_nerfs['half_damage_to']:
        print(value, end=' ') 

    print('\n\nInmune contra:')
    for value in pkmn_buffs_n_nerfs['no_damage_from']:
        print(value, end=' ') 

    print('\n\nIneficaz contra:')
    for value in pkmn_buffs_n_nerfs['no_damage_to']:
        print(value, end=' ')     
