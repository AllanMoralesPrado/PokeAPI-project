#Modulo encargado de cargar los archivos formato html en el navegador y eliminarlos
#del almacenamiento secundario dentro de unos segundos
import webbrowser
import os
import time

def show_pics(html, nombre):
    with open(f'{nombre}.html','w',encoding='utf8') as f:
        f.write(html)
    print('La información Pokémon solicitada se mostrará en tu Navegador Web...')
    time.sleep(2)
    webbrowser.open(f'{nombre}.html')
    time.sleep(5)
    os.remove(f'{nombre}.html')

if __name__ == '__main__':
    from get_evo import get_evolution
    from build_evo_html import build_evo_html
    from build_pokemon_html import build_html
    from get_base_info import get_base_pokemon
    from get_species_info import get_species
    from get_types import get_types_info

    name = 'gardevoir'
    base = get_base_pokemon(name)
    pre_evolution, description = get_species(name)
    pokemon_tipo, tipo_especial, pkmn_buffs_n_nerfs = get_types_info(name)

    html = build_html(name, base, pre_evolution, description, pokemon_tipo, tipo_especial, pkmn_buffs_n_nerfs)
    show_pics(html,'output')

    html = build_evo_html(name, get_evolution(name))
    show_pics(html,'evo_output')