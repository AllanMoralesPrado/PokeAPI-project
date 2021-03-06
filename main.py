#Archivo principal encargado de cargar un menú con características de UX y los módulos restantes del proyecto
#Para que el usuario ingrese el nombre de un pokemon valido y reciba información de este en el navegador la que es cargada
#desde una API REST
import time
import os
import sys
import data as d
import poke_validation as pv
from get_evo import get_evolution
from build_evo_html import build_evo_html
from build_pokemon_html import build_html
from get_base_info import get_base_pokemon
from get_species_info import get_species
from get_types import get_types_info
from show import show_pics

clear = 'cls' if sys.platform == 'win32' else 'clear'

print(d.WELCOME)
time.sleep(3)

while True:
    os.system(clear)
    opcion = int(input(d.MAIN_MENU))

    if opcion == 1:
        os.system(clear)
        name = input("Por favor, ingrese el nombre de un pokemon: ")
        name = pv.validate(name)
        opcion = int(input(d.MENU_1))
        if opcion == 1:
            base = get_base_pokemon(name)
            pre_evolution, description = get_species(name)
            pokemon_tipo, tipo_especial, pkmn_buffs_n_nerfs = get_types_info(name)

            html = build_html(name, base, pre_evolution, description, pokemon_tipo, tipo_especial, pkmn_buffs_n_nerfs)
            show_pics(html,'output_alpha')
        elif opcion == 2:
            html = build_evo_html(name, get_evolution(name))
            show_pics(html,'evo_output_alpha')
        elif opcion == 3:
            base = get_base_pokemon(name)
            pre_evolution, description = get_species(name)
            pokemon_tipo, tipo_especial, pkmn_buffs_n_nerfs = get_types_info(name)

            html = build_html(name, base, pre_evolution, description, pokemon_tipo, tipo_especial, pkmn_buffs_n_nerfs)
            show_pics(html,'output')
            
            html = build_evo_html(name, get_evolution(name))
            show_pics(html,'evo_output')
        else:
            print('Serás llevado al menú princial :)')
            time.sleep(3)
    else:
        print(d.BYEBYE)
        time.sleep(5)
        exit()