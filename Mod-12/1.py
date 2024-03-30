import requests
import json

pyyntö=requests.get('https://api.chucknorris.io/jokes/random').json()

print(pyyntö["value"])