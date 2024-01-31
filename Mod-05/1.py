import random

arpakuutiot = int(input("Syötä arpakuutioiden määrä "))
silmäluvut = [random.randint (1,6) for i in range (arpakuutiot)]
print (silmäluvut)
summa = sum (silmäluvut)
print (summa)