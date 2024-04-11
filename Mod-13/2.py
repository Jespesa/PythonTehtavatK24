from flask import Flask, Response, jsonify, request
import json
import mysql.connector

yhteys = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    database = "flight_game",
    user = "root",
    password = "12345",
    autocommit = True
)

app = Flask(__name__)
@app.route('/lentokentta/<icao>')
def kentta(icao):
    try:
        sql = f'SELECT ident, name, municipality FROM airport WHERE ident="{icao}"'
        print(sql)
        kursori = yhteys.cursor(dictionary=True)
        kursori.execute(sql)
        tulos = kursori.fetchall()
        return tulos


        tilakoodi = 200
        if tulos:
            vastaus = {
                "status": tilakoodi,
                "ICAO": tulos['ident'],
                "Name": tulos['name'],
                "Municipality": tulos['municipality']
            }
        else:
            raise ValueError
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "ICAO koodia vastaavaa lentokenttää ei löydy"
        }

    json_vastaus = json.dumps(vastaus)
    return Response(json_vastaus, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)