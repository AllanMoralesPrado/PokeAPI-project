from email.mime import base
from ssl import ALERT_DESCRIPTION_UNKNOWN_CA
import data as d
import time
import os
import sys
import poke_validation as pv
from get_module import get_info

clear = 'cls' if sys.platform == 'win32' else 'clear'

def traducir(lista):
    for i in range(len(lista)):
        type_to_tipo = get_info(lista[i])['names']
        for j in type_to_tipo:
            if j['language']['name'] == 'es':
                lista[i] = j['name']
                break

name = input("Nombre de pokemon: ")
name = pv.validate(name)

url_base = f'https://pokeapi.co/api/v2/pokemon/{name}'
url_species = f'https://pokeapi.co/api/v2/pokemon-species/{name}/'

resultado = get_info(url_base)
resultado_ = get_info(url_species)

#id y peso
pkmn_id = resultado['id']
pkmn_w = resultado['weight']

#evolucion anterior
pkmn_pre = ' '

if resultado_['evolves_from_species'] != None:
    pkmn_pre = resultado_['evolves_from_species']['name']
else:
    pkmn_pre = 'N/A'

print(pkmn_id)
print(pkmn_w)
print(pkmn_pre)

#stats
base_stat = [status['base_stat'] for status in resultado['stats']]
stat_name = [status['stat']['url'] for status in resultado['stats']]
traducir(stat_name)

pkmn_status = dict(zip(stat_name,base_stat))
print(pkmn_status)

#fortalezas/debilidades
#Ej: Charizard es tipo fuego, volador
double_damage_from = []
double_damage_to = []
half_damage_from = []
half_damage_to = []
no_damage_from = []
no_damage_to = []

#tipo/tipo especial
pkmn_type = [tipo['type']['url'] for tipo in resultado['types']]
print(pkmn_type)

for i in pkmn_type:
    tipo = get_info(i)['damage_relations']
    for j in tipo['double_damage_from']:
        double_damage_from.append(j['url'])
    for j in tipo['double_damage_to']:
        double_damage_to.append(j['url'])
    for j in tipo['half_damage_from']:
        half_damage_from.append(j['url'])
    for j in tipo['half_damage_to']:
        half_damage_to.append(j['url'])
    for j in tipo['no_damage_from']:
        no_damage_from.append(j['url'])
    for j in tipo['no_damage_to']:
        no_damage_to.append(j['url'])

traducir(double_damage_from)
double_damage_from = list(set(double_damage_from))
print(double_damage_from)
'''
print(double_damage_from)
print(half_damage_to)
print(half_damage_from)
print(no_damage_to)
print(no_damage_from)
'''
traducir(pkmn_type)
print(pkmn_type)

if resultado_['is_baby']:
    pkmn_type.append('Bebé')
if resultado_['is_legendary']:
    pkmn_type.append('Legendario')
if resultado_['is_mythical']:
    pkmn_type.append('Mítico')

print(pkmn_type)

#descripcion
descripcion = None
for i in get_info(url_species)['flavor_text_entries']:
    if i['language']['name'] == 'es':
        descripcion = i['flavor_text']
        break

print(descripcion)

#hola-a-todos