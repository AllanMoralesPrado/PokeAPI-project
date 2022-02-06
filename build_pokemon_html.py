def counter_span(counter):
    span_counter = ''
    for type in counter:
        span_counter += f'''<span class="label {type['name']}">{type['url']}</span>
        '''
    return span_counter

def build_html(id, name, wght, stat, sprite, pre_evo, desc, type, type_en, special_t, counters):
    
    #Elementos para la etiqueta <table> (stat)
    html_table_data_set = ''
    for key in stat:
        html_table_data_set += f'''<td><h5>{key}: {stat[key]}</h5></td>
        '''

    html_table = f'''
    <table>
        <tr>
            {html_table_data_set}
        </tr>
    </table>
    '''
    
    #Conjunto de <span> para cada tipo del pokemon
    html_type_set = ''
    for i, j in zip(type_en, type):
        html_type_set += f'''<span class="label {i}">{j}</span>
        '''

    if special_t:
        for i in special_t:
            html_type_set += f'''<span class="label normal">{i}</span>
            '''
    
    #Ventajas y desventajas
    html_counter_set = f'''<h3>Super efectivo contra:</h3>
        {counter_span(counters['double_damage_to'])}
    <h3>Débil contra:</h3>
        {counter_span(counters['double_damage_from'])}
    <h3>Resistente contra:</h3>
        {counter_span(counters['half_damage_to'])}
    <h3>Poco Eficaz contra:</h3>
        {counter_span(counters['half_damage_from'])}
    <h3>Inmune contra:</h3>
        {counter_span(counters['no_damage_to'])}
    <h3>Ineficaz contra:</h3>
        {counter_span(counters['no_damage_from'])}
    '''

    pkmn_html_body = f'''
    <div class="column2">
        <div class="card">
            <h1>#{id} {name.capitalize()}</h1>
            <img src="{sprite}" width="150" height="150">
            <div class="container">
                <h4>Etapa Previa: {pre_evo.capitalize()}</h4>
                <h4>Peso: {wght/10} Kg.</h4>
                <h2>Estadísticas</h2>
                {html_table}
                <h3><b>Tipo</b></h3> 
                    {html_type_set}
                    
                <p>{desc}</p>
                
                {html_counter_set}
            </div>
        </div>
    </div>
    '''


    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>#{id} {name.capitalize()}</title>
        <link rel="stylesheet" href="./mystyle.css">
    </head>
    <body>
        {pkmn_html_body}
    </body>
    </html>
    '''
    return html


if __name__ == '__main__':
    from get_base_info import get_base_pokemon
    from get_species_info import get_species
    from get_types import get_types_info
    from show import show_pics

    name = 'lucario'
    id, weight, stats, sprite = get_base_pokemon(name)
    pre_evolution, description = get_species(name)
    pokemon_tipo, pokemon_tipo_en, tipo_especial, pkmn_buffs_n_nerfs = get_types_info(name)

    html = build_html(id,name,weight,stats,sprite,pre_evolution,description,pokemon_tipo,pokemon_tipo_en,tipo_especial,pkmn_buffs_n_nerfs)
    show_pics(html,'output_alpha')