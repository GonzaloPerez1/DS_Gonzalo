import requests

def get_data():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json];
    (
    node["amenity"="school"]
    (around: 200, 40.360665, -3.612439, 40.373330, -3.637127, 40.373734, -3.597341, 40.381565, -3.624042);
    node["amenity"="fuel"]
    (around: 200, 40.360665, -3.612439, 40.373330, -3.637127, 40.373734, -3.597341, 40.381565, -3.624042);
    );
    out;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})

    print(response)
    data = response.json()
    return data

# , 40.886137, -3.569406, 40.893752, -3.570091