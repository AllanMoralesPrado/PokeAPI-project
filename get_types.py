from get_module import get_info

def url_base(name):
    return f'https://pokeapi.co/api/v2/pokemon/{name}'

def url_species(name):
    return f'https://pokeapi.co/api/v2/pokemon-species/{name}/'

def traducir(lista):
    for i in range(len(lista)):
        type_to_tipo = get_info(lista[i])['names']
        for j in type_to_tipo:
            if j['language']['name'] == 'es':
                lista[i] = j['name']
                break

resultado = get_info(url_base)
resultado_ = get_info(url_species)

#stats
base_stat = [status['base_stat'] for status in resultado['stats']]
stat_name = [status['stat']['url'] for status in resultado['stats']]
traducir(stat_name)

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
pkmn_type = [tipo['type']['url'] for tipo in resultado['types']]

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
    #Comprobar los efectos de la iteración (opcional)
    print(pkmn_damage_rel[i])

traducir(pkmn_type)

if resultado_['is_baby']:
    pkmn_type.append('Bebé')
if resultado_['is_legendary']:
    pkmn_type.append('Legendario')
if resultado_['is_mythical']:
    pkmn_type.append('Mítico')

print(pkmn_type)

if __name__ == '__main__':
    pass
