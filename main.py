import time
import os
import sys
import poke_validation as pv
from get_module import get_info

clear = 'cls' if sys.platform == 'win32' else 'clear'

name = input("Nombre de pokemon: ")
name = pv.validate(name)

while True:
    os.system(clear)
    opcion = input(d.MENU)
    opcion = int(validate(['0','1','2','3'], opcion))

    if opcion == 1:
        os.system(clear)
        n = int(input(d.APOD))
        print('Estamos procesando tus fotos...')
        id_foto = pull_fotos(n)
        html = create_html_pic(id_foto)
        show_pics(html, 'apod')
        time.sleep(3)
    elif opcion == 2:
        os.system(clear)
        planeta = input(d.PLANETA)
        planeta = int(validate(['1','2','3','4','5','6','7','8'], planeta))
        n = int(input('¿Cuántas fotos quiere ver? > '))
        print('Estamos procesando tus fotos...')
        titulos, descripcion, fotos = pull_planetas(planeta, n)
        html = create_html_planet(titulos, descripcion, fotos)
        show_pics(html, 'planetas')
        time.sleep(3)
    elif opcion == 3:
        os.system(clear)
        fecha = input(d.TIERRA)
        fotos, horas = pull_earth(fecha)
        html = create_html_earth(fotos, horas)
        show_pics(html, 'tierra')
        time.sleep(3)
    else:
        print('Gracias por venir')
        time.sleep(2)
        exit()