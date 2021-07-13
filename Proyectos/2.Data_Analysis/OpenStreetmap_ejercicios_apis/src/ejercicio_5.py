import requests
import pandas as pd
import plotly.express as px

from config import MAPBOX_TOKEN

def get_data():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json];
    area[name="Sevilla"];
    node[amenity=restaurant](area);
    out;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})

    print(response)
    data = response.json()
    return data

def json_to_df():
    data = get_data()
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
                      color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=11,
                      hover_name="name")
    fig.update_layout(
        mapbox=dict(
            accesstoken = MAPBOX_TOKEN
        )
    )

    fig.show()

plot_data()