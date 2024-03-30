import requests
import json

def get_weather():
    Kysely = input("Anna Paikkakunta: ")
    apikey = '2029dcdc8dfcbd3ba517f903998f9239'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={Kysely}&appid={apikey}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        celsius = round(temp - 273.15, 1)
        return temp, celsius

    else:
        print("Kaupunkia ei löytynyt.")
        return None

sää = get_weather()
if sää is not None:
    lämpötila_kelvin, lämpötila_celsius = sää
    print(f"Lämpötila on: {lämpötila_celsius:.1f} °C")

