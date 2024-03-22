class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self,muutos):
        self.tamanhetkinen_nopeus += muutos
        if self.tamanhetkinen_nopeus <= 0:
            self.tamanhetkinen_nopeus = 0
        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus

auto = Auto("ABC-123", 142,)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print (auto.tamanhetkinen_nopeus)

auto.kiihdytä(-200)

print (auto.tamanhetkinen_nopeus)