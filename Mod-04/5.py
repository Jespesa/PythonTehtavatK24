yritykset = 0

while yritykset < 5:
    käyttäjätunnus = input ("Syötä käyttäjätunnus: ")
    salasana = input ("Syötä salasana ")
    if käyttäjätunnus == "python" and salasana == "rules":
        print ("Tervetuloa")
        break

    else:
        print ("Pääsy evätty")
        yritykset +=1
    if yritykset == 5:
        print ("Yritykset ylittyivät")
        exit()