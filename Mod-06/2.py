import random

noppa = int(input("Anna nopan maksimisilmäluku: "))
def heitä():
    tulos = random.randint(1,noppa)
    return tulos

x= heitä()

while x !=heitä():
    print (f"Heiton tulos oli {x}")
    x = heitä()
    if x ==heitä():
        print(f"Sait nopan maksimisilmäluvun: {noppa}")
        break