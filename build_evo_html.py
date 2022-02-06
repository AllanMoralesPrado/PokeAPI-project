def Preevolucion(nombre):
    if nombre != 'No tiene':
        return f'<h4>Etapa Previa: {nombre.capitalize()}</h4>'
    else:
        return ''

def tipo(lista_tipos, lista_tipos_en):
    tipos = ''
    for es, en in zip(lista_tipos, lista_tipos_en):
        tipos += f'''<span class="label {en}">{es}</span>
        '''
    return tipos

def spec_types(lista_especiales):
    special = ''
    if lista_especiales:
        for i in lista_especiales:
            special += f'''<span class="label normal">{i}</span>
            '''
    return special

def lvl1(chain):
    lvl_1_content = f'''<h1>Nivel 1</h1>
    '''

    for pokemon in chain:
        lvl_1_content += f'''<div class="row">   
            <div class="column1">
                <div class="card">
                    <h1>#{pokemon['id']} {pokemon['name'].capitalize()}</h1>
                    <img src={pokemon['sprite']} width="150" height="150">
                    <div class="container">
                        {Preevolucion(pokemon['pre_evo'])}
                        <h3><b>Tipo</b></h3> 
                        {tipo(pokemon['types'],pokemon['types_en'])}
                        {spec_types(pokemon['spec'])}
                    </div>
                </div>
            </div>
        </div>
        '''
    return lvl_1_content

def lvl2(chain):
    lvl_2_content = ''
    if chain:
        lvl_2_content += f'''<h1>Nivel 2</h1>
        '''

        for pokemon in chain:
            lvl_2_content += f'''<div class="row">   
                <div class="column1">
                    <div class="card">
                        <h1>#{pokemon['id']} {pokemon['name'].capitalize()}</h1>
                        <img src={pokemon['sprite']} width="150" height="150">
                        <div class="container">
                            {Preevolucion(pokemon['pre_evo'])}
                            <h3><b>Tipo</b></h3> 
                            {tipo(pokemon['types'],pokemon['types_en'])}
                            {spec_types(pokemon['spec'])}
                        </div>
                    </div>
                </div>
            </div>
            '''
    return lvl_2_content

def lvl3(chain):
    lvl_3_content = ''
    if chain:
        lvl_3_content += f'''<h1>Nivel 3</h1>
        '''

        for pokemon in chain:
            lvl_3_content += f'''<div class="row">   
                <div class="column1">
                    <div class="card">
                        <h1>#{pokemon['id']} {pokemon['name'].capitalize()}</h1>
                        <img src={pokemon['sprite']} width="150" height="150">
                        <div class="container">
                            {Preevolucion(pokemon['pre_evo'])}
                            <h3><b>Tipo</b></h3> 
                            {tipo(pokemon['types'],pokemon['types_en'])}
                            {spec_types(pokemon['spec'])}
                        </div>
                    </div>
                </div>
            </div>
            '''
    return lvl_3_content

def build_evo_html(name, evo_list):

    pkmn_html_body = f'''{lvl1(evo_list[0])}
    
    {lvl2(evo_list[1])}

    {lvl3(evo_list[2])}'''    

    html = f'''
    <!DOCTYPE html>
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{name.capitalize()} (cadena evolutiva)</title>
            <link rel="stylesheet" href="./mystyle.css">
        </head>
        <body>
            {pkmn_html_body}
        </body>
    </html>
    '''
    return html

if __name__ == '__main__':
    from get_evo import get_evolution
    from show import show_pics

    name = 'lucario'
    html = build_evo_html(name, get_evolution(name))
    show_pics(html,'evo_output_alpha')