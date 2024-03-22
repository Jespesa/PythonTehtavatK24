class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

uusiauto = Auto (f"ABC-123",142)

print(f"Uuden auton rekisteritunnus on {uusiauto.rekisteritunnus} ja sen huippunopeus on {uusiauto.huippunopeus} km/h")