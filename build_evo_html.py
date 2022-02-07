from build_pokemon_html import type_span

def Preevolucion(nombre):
    if nombre != 'No tiene':
        return f'<h4>Etapa Previa: {nombre.capitalize()}</h4>'
    else:
        return ''

def spec_types(lista_especiales):
    special = ''
    if lista_especiales:
        for i in lista_especiales:
            special += f'''<span class="label normal">{i}</span>
            '''
    return special

def lvl(chain):
    lvl_content = ''

    for pokemon in chain:
        lvl_content += f'''<div class="row">   
            <div class="column1">
                <div class="card">
                    <h1>#{pokemon['id']} {pokemon['name'].capitalize()}</h1>
                    <img src={pokemon['sprite']} width="150" height="150">
                    <div class="container">
                        {Preevolucion(pokemon['pre_evo'])}
                        <h3><b>Tipo</b></h3> 
                        {type_span(pokemon['types'])}
                        {spec_types(pokemon['spec'])}
                    </div>
                </div>
            </div>
        </div>
        '''
    return lvl_content

def build_evo_html(name, evo_list):

    pkmn_html_body = f'''<h1>Nivel 1</h1>
    {lvl(evo_list[0])}
    '''    

    if evo_list[1]:
        pkmn_html_body += f'''<h1>Nivel 2</h1>
        {lvl(evo_list[1])}
        ''' 
    if evo_list[2]:
        pkmn_html_body += f'''<h1>Nivel 3</h1>
        {lvl(evo_list[2])}
        ''' 

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

    name = 'eevee'
    html = build_evo_html(name, get_evolution(name))
    show_pics(html,'evo_output_alpha')