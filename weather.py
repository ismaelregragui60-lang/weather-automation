import requests
import json
from datetime import datetime

url = "https://api.open-meteo.com/v1/forecast?latitude=41.38&longitude=2.17&daily=temperature_2m_max,temperature_2m_min&timezone=auto"

data = requests.get(url).json()

maxima = data["daily"]["temperature_2m_max"][0]
minima = data["daily"]["temperature_2m_min"][0]
mitjana = (maxima + minima) / 2

resultat = {
    "maxima": maxima,
    "minima": minima,
    "mitjana": mitjana
}

nom = f"temp_{datetime.now().strftime('%Y%m%d')}.json"

with open(nom, "w") as f:
    json.dump(resultat, f, indent=4)

print("Fitxer JSON creat")