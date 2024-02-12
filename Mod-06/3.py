g = 1
def laskuri (g):
    tulos = g * 3.785
    print(tulos)

while g > 0:
    g = float(input("Syötä gallonamäärä, negatiivinen lopettaa: "))
    laskuri (g)
else:
    print ("Ohjelma loppui")