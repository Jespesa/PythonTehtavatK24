import random

noppa = int(input("Anna nopan maksimisilmäluku: "))
def heitä(noppa):
    tulos = random.randint(1,noppa)
    return tulos

x= heitä(noppa)

while x !=noppa:
    print (f"Heiton tulos oli {x}")
    x = heitä(noppa)
    if x ==noppa:
        print(f"Sait nopan maksimisilmäluvun: {noppa}")
        break