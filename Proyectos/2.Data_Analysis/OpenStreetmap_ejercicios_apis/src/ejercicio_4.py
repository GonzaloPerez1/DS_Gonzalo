import requests

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