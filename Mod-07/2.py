nimet = set ()

name = "dummy"

while name != "":
    name = input ("Anna nimi: ")
    if name in nimet:
        print ("Nimi on jo annettu")
    else:
        if name != "":
            print ("Uusi nimi")
            nimet.add (name)
for nimi in nimet:
    print (nimi)