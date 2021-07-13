import requests

def get_data():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json];
    area["name"="Madrid"]["admin_level"="8"][boundary=administrative];
    node["amenity"="hospital"](area);
    out;
    area["name"="Madrid"]["admin_level"="8"][boundary=administrative];
    node["amenity"="clinic"](area);
    out;
    area["name"="Madrid"]["admin_level"="8"][boundary=administrative];
    node["amenity"="bbq"](area);
    out;
    area["name"="Madrid"]["admin_level"="8"][boundary=administrative];
    node["amenity"="drinking_water"](area);
    out;
    area["name"="Madrid"]["admin_level"="8"][boundary=administrative];
    node["amenity"="kindergarten"](area);
    out;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})

    print(response)
    data = response.json()
    return data

#[admin_level=6][boundary=administrative]