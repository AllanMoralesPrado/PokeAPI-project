from email.mime import base
from ssl import ALERT_DESCRIPTION_UNKNOWN_CA
import data as d
import time
import os
import sys
import poke_validation as pv
from get_module import get_info

clear = 'cls' if sys.platform == 'win32' else 'clear'

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
d.traducir(stat_name)

pkmn_status = dict(zip(stat_name,base_stat))
print(pkmn_status)

#descripcion
descripcion = None
for i in get_info(url_species)['flavor_text_entries']:
    if i['language']['name'] == 'es':
        descripcion = i['flavor_text']
        break

print(descripcion)

#hola-a-todos
#como estan