from get_module import get_info

def validacion_pokemon():
    return "Introduce el nombre de un pokemon: "

def traducir(lista):
    for i in range(len(lista)):
        type_to_tipo = get_info(lista[i])['names']
        for j in type_to_tipo:
            if j['language']['name'] == 'es':
                lista[i] = j['name']
                break
    return lista