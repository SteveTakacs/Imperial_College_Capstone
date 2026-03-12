# Pokemon TCG API
# https://docs.pokemontcg.io/

import time
import requests

url = "https://api.pokemontcg.io/v2/cards"
params = {
    "q": 'name:"Charizard"',
    "pageSize": 10,
    "select": "id,name,rarity,number,set"
}

for attempt in range(3):
    try:
        response = requests.get(url, params=params, timeout=30)
        print("Status:", response.status_code)
        response.raise_for_status()
        data = response.json()["data"]
        print(f"Siker, {len(data)} kártya érkezett.")
        print(data[:2])
        break
    except requests.exceptions.HTTPError as e:
        print("HTTP hiba:", e)
        print("Válasz eleje:", response.text[:300])
        if response.status_code in [500, 502, 503, 504] and attempt < 2:
            print("Újrapróbálás...")
            time.sleep(3)
        else:
            raise
    except requests.exceptions.RequestException as e:
        print("Kapcsolati hiba:", e)
        if attempt < 2:
            print("Újrapróbálás...")
            time.sleep(3)
        else:
            raise