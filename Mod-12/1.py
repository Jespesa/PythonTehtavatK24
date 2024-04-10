import requests

pyyntö=requests.get('https://api.chucknorris.io/jokes/random').json()

print("Tässä sinulle Chuck Norris vitsi: ")
print(pyyntö["value"])