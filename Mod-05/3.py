alkuluku = True
kokonaisluku = int (input ("Syötä kokonaisluku "))

for jakaja in range (2,kokonaisluku):
    if kokonaisluku % jakaja ==0:
        alkuluku = False
        break
if alkuluku == True:
    print ("Kokonaisluku on alkuluku")


else:print ("Kokoanaisluku ei ole alkuluku")