from get_module import get_info

def validacion_pokemon():
    return "Introduce el nombre de un pokemon: "

def traducir(lista):
    for i in range(len(lista)):
        if type(lista[i]) is str:
            type_to_tipo = get_info(lista[i])['names']
            for j in type_to_tipo:
                if j['language']['name'] == 'es':
                    lista[i] = j['name']
                    break
        elif type(lista[i]) is dict:
            type_to_tipo = get_info(lista[i]['url'])['names']
            for j in type_to_tipo:
                if j['language']['name'] == 'es':
                    lista[i]['url'] = j['name']
                    break
    return lista

WELCOME = """
                ██████╗░░█████╗░██╗░░██╗███████╗██████╗░███████╗██╗░░██╗
                ██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔════╝╚██╗██╔╝
                ██████╔╝██║░░██║█████═╝░█████╗░░██║░░██║█████╗░░░╚███╔╝░
                ██╔═══╝░██║░░██║██╔═██╗░██╔══╝░░██║░░██║██╔══╝░░░██╔██╗░
                ██║░░░░░╚█████╔╝██║░╚██╗███████╗██████╔╝███████╗██╔╝╚██╗
                ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝
            
Bienvenido a la app Pokédex, donde puedes encontrar información de los Pokémon que quieras :D

                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@&&#BGGGPPPGGB#&&@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@&BP555555555555555PGB#@@@@@@@@@@@@@@
                    @@@@@@@@@@@@BP555555555555555555555PPB&@@@@@@@@@@@
                    @@@@@@@@@@#P555555555555555555555555PPPB@@@@@@@@@@
                    @@@@@@@@@G555555555555555555555555555PPPG&@@@@@@@@
                    @@@@@@@@G55555555555PGB&&&&BGP55555555PPPG&@@@@@@@
                    @@@@@@@B55555555555B@@&G55G&@@B5555555PPP5G@@@@@@@
                    @@@@@@@GPPPPPPPPPP#@@J.    .J@@#PPPPPPGGGGG@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@#        #@@@@@@@@@@@@@@@@@@@@
                    @@@@@@&~^^^^^^^^^^P@@Y.    .J@@P^^^^^^~!!!?@@@@@@@
                    @@@@@@@!           J&@&G55G&@&J       .::.5@@@@@@@
                    @@@@@@@#:           .!YPGGPY!.       .::.7@@@@@@@@
                    @@@@@@@@#^                          .:::?@@@@@@@@@
                    @@@@@@@@@&J.                       .:.~P@@@@@@@@@@
                    @@@@@@@@@@@#?:                    .:!5&@@@@@@@@@@@
                    @@@@@@@@@@@@@&P?^.              :!YB@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@#GY?7!~~~~!7J5B&@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

                             __          ___   ____            
                            / /  __ __  / _ | / / /__ ____     
                           / _ \/ // / / __ |/ / / _ `/ _ \    
                          /_.__/\_, / /_/ |_/_/_/\_,_/_//_/    
                               /___/                           """

MAIN_MENU = """¿Qué desea hacer?

    1. \"Busco a un Pokémon\"
    2. \"Necesito irme de aquí\"

    > """

MENU_1 = """¿Qué información desea conocer sobre ese Pokémon?

    1. Datos Generales
    2. Cadena Evolutiva
    3. Opciones 1 y 2
    0. \"Ya tengo lo que necesito\"
    
    > """

BYEBYE = f"""
Gracias por venir y recuerda...
ATRÁPALOS TODOS!!!
"""