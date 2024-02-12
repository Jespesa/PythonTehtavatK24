vuodenajat = ("kevät","kesä","syksy","talvi")

kuukausi = int(input("Syötä kuukauden numero " ))

if kuukausi >= 1 and kuukausi <3 or kuukausi ==12:
    print (f"Vuodenaika on {vuodenajat[3]}")
elif kuukausi >= 3 and kuukausi <=5:
    print (f"Vuodenaika on {vuodenajat[0]}")
elif kuukausi >= 6 and kuukausi <=8:
    print (f"Vuodenaika on {vuodenajat[1]}")
else:
    print (f"Vuodenaika on {vuodenajat[2]}")