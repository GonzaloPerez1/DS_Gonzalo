import pandas as pd
import plotly.express as px

from config import MAPBOX_TOKEN

import ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4

lista_ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4]

def json_to_df():
    position = int(input("Coloca un número del ejercicio que quieras (empieza en 0): "))
    ejercicio = lista_ejercicios[position]

    data = ejercicio.get_data()
    elements = data['elements']
    places = {'tipo': [], 'lat': [], 'lon': [], 'name': [], 'address': []}

    for i in elements:

        tipo = i.get('tags', None).get('amenity', None)
        latitude = i.get('lat', None)
        longitude = i.get('lon', None)
        name = i.get('tags', {}).get('name', "NO NAME")
        street = i.get('tags', {}).get('addr:street', "NO STREET")
        number = i.get('tags', {}).get('addr:housenumber', 9999)

        places['tipo'].append(tipo)
        places['lat'].append(latitude)
        places['lon'].append(longitude)
        places['name'].append(name)
        places['address'].append(street + ' ' + str(number))


    return pd.DataFrame(places)

def plot_data():
    df = json_to_df()
    print(df.head())
    print(type(df))
    fig = px.scatter_mapbox(df,
                            lat="lat",
                            lon="lon",
                            color = "tipo",
                      color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=11)
    fig.update_layout(
        mapbox=dict(
            accesstoken = MAPBOX_TOKEN
        )
    )

    fig.show()

plot_data()