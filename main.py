from api.getCityLongLat import getCityLongLat
from api.searchNearby import searchNearby
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GOOGLE_TOKEN")
city = input("Enter city: ")
cords = getCityLongLat(city,key=api_key)
resp = searchNearby(cords[0], cords[1], 500, api_key)

for r in resp:
   print(r.mapsUrl)
   print(r.name)
   print(r.rating)