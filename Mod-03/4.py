vuosiluku=int(input("Syötä vuosiluku: "))
if vuosiluku % 4==0:
    if vuosiluku % 100!=0 or vuosiluku % 400==0:
        print ("Vuosiluku on karkausvuosi")
    else:print ("Vuosi ei ole karkausvuosi")
else:print ("Vuosi ei ole karkausvuosi")