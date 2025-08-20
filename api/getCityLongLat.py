import requests

def getCityLongLat(city, key):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": city,
        "key": key
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(response.json())
    data = response.json()
    lat = data["results"][0]["geometry"]["location"]["lat"]
    lng = data["results"][0]["geometry"]["location"]["lng"]
    return lat, lng