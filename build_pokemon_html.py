#Modulo encargado de generar un str que contiene texto compatible con codigo html
#A partir de patrones de etiquetado en funcion de los datos del pokemon ingresados
def type_span(counter):
    dtypes = {
        "normal": "Normal", "fire": "Fuego", "flying": "Volador",
        "steel": "Acero", "water": "Agua", "electric": "Eléctrico",
        "grass": "Planta", "ice": "Hielo", "fighting": "Lucha",
        "poison": "Veneno", "ground": "Tierra", "psychic": "Psíquico",
        "bug": "Bicho", "rock": "Roca", "ghost": "Fantasma",
        "dragon": "Dragón", "dark": "Siniestro", "steel": "Acero",
        "fairy": "Hada" 
    }
    span_counter = ''
    for type in counter:
        counter_es = dtypes.get(type)
        span_counter += f'''<span class="label {type}">{counter_es}</span>
        '''
    return span_counter

def build_html(name, base, pre_evolution, description, pokemon_tipo, tipo_especial, pkmn_buffs_n_nerfs):
    
    #Elementos para la etiqueta <table> (stat)
    stat_name = ['PS','Ataque','Defensa','Ataque Especial','Defensa Especial','Velocidad']
    html_table_data_set = ''
    for key,value in zip(stat_name,base['stats']):
        html_table_data_set += f'''<td><h5>{key}: {value}</h5></td>
        '''

    html_table = f'''
    <table>
        <tr>
            {html_table_data_set}
        </tr>
    </table>
    '''
    
    #Conjunto de <span> para cada tipo del pokemon
    html_type_set = f'{type_span(pokemon_tipo)}'

    if tipo_especial:
        for i in tipo_especial:
            html_type_set += f'''<span class="label normal">{i}</span>
            '''
    
    #Ventajas y desventajas
    html_counter_set = f'''<h3>Super efectivo contra:</h3>
        {type_span(pkmn_buffs_n_nerfs['double_damage_to'])}
    <h3>Débil contra:</h3>
        {type_span(pkmn_buffs_n_nerfs['double_damage_from'])}
    <h3>Resistente contra:</h3>
        {type_span(pkmn_buffs_n_nerfs['half_damage_to'])}
    <h3>Poco Eficaz contra:</h3>
        {type_span(pkmn_buffs_n_nerfs['half_damage_from'])}
    <h3>Inmune contra:</h3>
        {type_span(pkmn_buffs_n_nerfs['no_damage_to'])}
    <h3>Ineficaz contra:</h3>
        {type_span(pkmn_buffs_n_nerfs['no_damage_from'])}
    '''

    pkmn_html_body = f'''
    <div class="column2">
        <div class="card">
            <h1>#{base['id']} {name.capitalize()}</h1>
            <img src="{base['pkmn_sprite']}" width="150" height="150">
            <div class="container">
                <h4>Etapa Previa: {pre_evolution.capitalize()}</h4>
                <h4>Peso: {base['peso']/10} Kg.</h4>
                <h2>Estadísticas</h2>
                {html_table}
                <h3><b>Tipo</b></h3> 
                    {html_type_set}
                    
                <p>{description}</p>
                
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
        <title>#{base['id']} {name.capitalize()}</title>
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
    base = get_base_pokemon(name)
    pre_evolution, description = get_species(name)
    pokemon_tipo, tipo_especial, pkmn_buffs_n_nerfs = get_types_info(name)

    html = build_html(name, base, pre_evolution, description, pokemon_tipo, tipo_especial, pkmn_buffs_n_nerfs)
    show_pics(html,'output')