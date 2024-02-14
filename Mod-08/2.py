import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1235',
    autocommit=True,
)


def hae_maakoodi(maakoodi):
    mycursor = yhteys.cursor()
    mycursor.execute("SELECT name FROM airport WHERE iso_country like '" + maakoodi + "'")
    myresult = mycursor.fetchall()

    for i in myresult:
        print(i)
    return


i = input("Syötä maakoodin: ")
hae_maakoodi(i)