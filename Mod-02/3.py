import math
kanta = float(input("Syötä suorakulmion kannan pituus"))
korkeus = float(input("Syötä suorakulmion korkeus"))
piiri = float(kanta + kanta + korkeus + korkeus)
pinta_ala = float(kanta * korkeus)
print ("Suorakulmion piiri on " +str (piiri))
print ("Suorakulmion pinta-ala on "+str(pinta_ala))