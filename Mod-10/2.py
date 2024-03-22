class Hissi:
    def __init__(self,alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        #missä kerroksessa nyt ollaan ?
        self.kerros = alin_kerros           # Hissi on aina alimmassa kerroksessa

    # hissi siirtyy haluttuun kerrokseen
    def siirry_kerrokseen(self, tavoite):
        # siirrytäänkö ylöspäin ?
        if tavoite > self.kerros:
            # niin kauan kun hissi on liian alhaalla, niin siirrytään kerros ylöspäin
            while self.kerros < tavoite:
                self.kerros_ylös()
            #siirrytäänkö alaspäin ?
        elif tavoite < self.kerros:
            while self.kerros > tavoite:
                self.kerros_alas()

            print ("Hissi on halutussa kerroksessa")
        return

    # hissi siirtyy yhden kerroksen ylöspäin
    def kerros_ylös(self):
        # siirrytään ylös vain jos ei olla ylimmässä kerroksessa
        if self.kerros < self.ylin_kerros:
            self.kerros = self.kerros + 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

    def kerros_alas(self):
        # Siirrytään alaspäin vain jos ei olla alimmassa kerroksessa
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

#Määritellään Talo-luokka
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, lukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lukumäärä = lukumäärä
        self.hissit = []                   #Tyhjä lista talon hissejä varten
        # Luodaan talon hissit ja lisätään ne hissit nimiseen listaan
        for i in range (lukumäärä):
            # Luodaan uusi hissi
            uusiHissi = Hissi(self.alin_kerros, self.ylin_kerros)
            # Lisätään luoto olio hissit-listaan
            self.hissit.append(uusiHissi)

    def aja_hissiä(self, hissin_nro, kohdekerros):
        # Sopimus: hissit numeroidaan 1, 2, 3,....
        # Etsitään oikea hissi, siitä tulee Hissi-tyyppinen olio
        ajettavaHissi = self.hissit[hissin_nro - 1]
        # Ajetaan hissi kohdekerrokseen
        ajettavaHissi.siirry_kerrokseen(kohdekerros)

# PÄÄOHJELMA
# Luon uuden talon, 3kpl hissejä
ekaTalo = Talo(1,10,3)
# Ajetaan eka hissi 3. kerrokseen
ekaTalo.aja_hissiä(1,3)

# Etsitään talon eka hissi
ekaHissi = ekaTalo.hissit[0]
print (f"Eka hissi on kerroksessa {ekaHissi.kerros}")
print (f"Vika hissi on kerroksessa {ekaTalo.hissit[2].kerros}")
