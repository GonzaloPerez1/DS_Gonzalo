import requests

def get_data():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json];
    node["amenity"="parking"]
        (40.419498, -3.693327, 40.437643, -3.677456);
    out;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})

    print(response)
    data = response.json()
    return data
