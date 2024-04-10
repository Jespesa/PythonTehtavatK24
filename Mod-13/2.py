from flask import Flask, jsonify

app = Flask(__name__)

# Tässä voit simuloida tietokantaa, jossa on lentokenttätiedot
lentokentatietokanta = {
    "EFHK": {"Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"},
    "EGLL": {"Name": "Heathrow Airport", "Municipality": "London"},
    # Lisää muita lentokenttäkoodeja ja niiden tietoja tarvittaessa
}

#hae kenttää syöttämällä urliin esim /kenttä/EFHK
@app.route('/kenttä/<string:koodi>', methods=['GET'])
def hae_lentokentta(koodi):
    lentokentta = lentokentatietokanta.get(koodi)
    if lentokentta:
        lentokentta["ICAO"] = koodi
        return jsonify(lentokentta)
    else:
        return jsonify({"error": "Lentokenttää ei löydy"}), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)