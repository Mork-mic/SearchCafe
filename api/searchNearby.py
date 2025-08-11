import json
import requests
from models.placeModel import Place


def searchNearby(latitude, longitude, radius, apiKey):
    url = "https://places.googleapis.com/v1/places:searchNearby"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": apiKey,
        "X-Goog-FieldMask": "places.displayName,places.googleMapsUri,places.rating"
    }

    data = {
        "includedTypes": ["cafe"],
        "maxResultCount": 10,
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": f"{latitude}",
                    "longitude": f"{longitude}"
                },
                "radius": f"{radius}"
            }
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        raise Exception(response.json())
    output = []
    for place in response.json()["places"]:
        model = Place(place['displayName']['text'], place['googleMapsUri'], place['rating'])
        output.append(model)
    return output