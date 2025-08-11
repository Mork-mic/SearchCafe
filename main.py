from api.searchNearby import searchNearby
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GOOGLE_TOKEN")

resp = searchNearby(53.987407, 27.671146, 500, api_key)

for r in resp:
    print(r.mapsUrl)
    print(r.name)
    print(r.rating)