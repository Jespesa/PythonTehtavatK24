class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja}")


# Luodaan julkaisut
aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_no_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

# Tulostetaan julkaisujen tiedot
print("Aku Ankka:")
aku_ankka.tulosta_tiedot()
print("\nHytti n:o 6:")
hytti_no_6.tulosta_tiedot()
