#Módulo encargado de validar el nombre del pokemon que ingrese el usuario
# dándole un formato para proceder la consulta a un archivo externo que contiene una lista de nombres
# si no existen coincidencias, se le muestra un mensaje al usuario con indicaciones adicionales hasta
# que exista una coincidencia exitosa
import sys
import os

clear = 'cls' if sys.platform == 'win32' else 'clear'

with open("pokemon_list.txt", "r") as f:
    pokemon_lista = f.readlines()
    
pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista]
import data as d

def validate(name, p_l = pokemon_lista, mensaje = d.validacion_pokemon()):
    if name =='codigo-cero':
        name = 'type-null'
    while name not in p_l:
        os.system(clear)
        name = input(mensaje).lower()

    return name

if __name__ == '__main__':
    name = 'codigo-cero'
    print(validate(name))
