class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 60
        self.kuljettu_matka = 2000

    def kiihdytä(self,muutos):
        self.tamanhetkinen_nopeus += muutos
        if self.tamanhetkinen_nopeus <= 0:
            self.tamanhetkinen_nopeus = 0
        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus

    def kulje(self,tuntimäärä):
        matka = self.tamanhetkinen_nopeus * tuntimäärä
        self.kuljettu_matka += matka

auto = Auto("ABC-123", 142,)

auto.kulje(1.5)
auto.kiihdytä(60)
print(auto.kuljettu_matka)
