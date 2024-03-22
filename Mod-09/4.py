import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.tamanhetkinen_nopeus += muutos
        if self.tamanhetkinen_nopeus <= 0:
            self.tamanhetkinen_nopeus = 0
        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus

    def kulje(self, tuntimäärä):
        matka = self.tamanhetkinen_nopeus * tuntimäärä
        self.kuljettu_matka += matka

# Luo autot
autojen_lkm = 10
autot = []
for i in range(autojen_lkm):
    auto = Auto(f"ABC-{i+1}", random.randint(100, 200))
    autot.append(auto)

# Kilpailu
kilpailuaika = 0
while True:
    kilpailuaika += 1
    print(f"\nKilpailuaika: {kilpailuaika} tuntia")
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)  # Liikuta autoa yhden tunnin ajan
        print(f"{auto.rekisteritunnus}: Nopeus={auto.tamanhetkinen_nopeus} km/h, Matka={auto.kuljettu_matka} km")
    # Tarkista, onko jokin auto kulkenut vähintään 10000 km
    if any(auto.kuljettu_matka >= 10000 for auto in autot):
        break

# Tulosta kunkin auton ominaisuudet taulukkomuodossa
print("\nAutot kilpailun jälkeen:")
print("{:<15} {:<15} {:<15} {:<15}".format("Rekisteritunnus", "Huippunopeus", "Nopeus", "Kuljettu matka"))
for auto in autot:
    print("{:<15} {:<15} {:<15} {:<15}".format(auto.rekisteritunnus, auto.huippunopeus, auto.tamanhetkinen_nopeus, auto.kuljettu_matka))