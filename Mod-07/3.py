airports = {"EFHK" : "Helsinki-Vantaan lentoasema"}

print("1 = haku, 2 = kentän lisäys, 3 = lopetus")

toiminto = 0

while toiminto != 3:
    toiminto = int(input("Valitse toiminto: "))

    if toiminto == 1:
        avain = input("Anna kentän ICAO-koodi: ")
        if avain in airports:
            print(f"Lentoaseman nimi on: {airports[avain]} ")
        else:
            print("Koodillasi ei löytynyt lentokenttää")

    elif toiminto == 2:
        kenttä = input("Lisää uusi kenttä: ")
        print(f"Uusi kenttä '{kenttä}' on lisätty")

    elif toiminto == 3:
        print("Ohjelma lopetetaan.")

    else:
        print("Virheellinen valinta")