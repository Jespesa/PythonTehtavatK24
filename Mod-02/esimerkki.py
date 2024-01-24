#Ehtolause (If)
#kysytään käyttäjän ikä
#muutetaan käyttäjän antama arvo heti kokonaisluvuksi
ika = int(input("Anna ikäsi: "))
if ika >=18:
    print ("Olet siis täysi-ikäinen")
    print ("Lähdetkö kahville ?")
elif ika <18:print ("MENE NUKKUMAAN")
print ("Ohjelma loppui")