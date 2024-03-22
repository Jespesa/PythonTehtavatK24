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

# Pääohjelma
# Luon uuden hissin
ekaHissi = Hissi(1, 7)
tokaHissi = Hissi(1, 7)
# Siirrytään kerrokseen 4
ekaHissi.siirry_kerrokseen(4)
tokaHissi.siirry_kerrokseen(2)