import random
def heitä():
    tulos = random.randint(1,6)
    return tulos

x= heitä()

while (x) !=6:
    print (f"Heiton tulos oli {x}")
    x = heitä()
    if (x) ==6:
        print("Sait numeron 6")
        break