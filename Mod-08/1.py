''''
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
'''
import mysql.connector

def get_airport_by_icao(icao):
    sql = f'select name, municipality, type FROM airport WHERE ident = "{icao}" OR ident = "EFHK"'
    print (sql)
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return result

db_connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='12345',
    autocommit=True
    )

icao = input ("Anna ICAO-koodi: ")

airports = get_airport_by_icao(icao)
print (airports)

for ap in airports:
    print (f"Nimi: {ap['name']}, joka sijaitsee kunnassa {ap['municipality']}")
    print (f"Sen tyyppi on {ap['type']}")


