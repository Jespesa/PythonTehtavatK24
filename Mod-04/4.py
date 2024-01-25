import random

arvottava = random.randint(1,10)

while True:
    luku =int(input("Syötä arvottava luku "))
    if luku == arvottava:
         print("Oikein !")
         break
    elif luku > arvottava:
        print ("Luku on liian suuri ")
    else: print ("Luku on liian pieni")