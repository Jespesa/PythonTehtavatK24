import random
# määritellään Auto-luokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        # alla olevia ominaisuuksia ei voi asettaa oliota luodessa
        self.nopeus = 0  # tämän hetken nopeus
        self.matka = 0  # auton kulkema matka

class Sähköauto(Auto):
    def __init__(self, akkukapasiteetti,rekisteritunnus,huippunopeus):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)


    def kiihdyta(self, muutos):
        # muutetaan auton nopeutta
        self.nopeus = self.nopeus + muutos
        # nopeus ei saa nousta yli huippunopeuden
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        # nopeus ei saa mennä negatiiviseksi
        if self.nopeus < 0:
            self.nopeus = 0
        return

    def kulje(self, aika):
        # lisätään auton kulkemaa matkaa
        self.matka += self.nopeus * aika
        return

class Polttomoottoriauto(Auto):
    def __init__(self, bensatankin_koko,rekisteritunnus,huippunopeus):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus)


    def kiihdyta(self, muutos):
        # muutetaan auton nopeutta
        self.nopeus = self.nopeus + muutos
        # nopeus ei saa nousta yli huippunopeuden
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        # nopeus ei saa mennä negatiiviseksi
        if self.nopeus < 0:
            self.nopeus = 0
        return

    def kulje(self, aika):
        # lisätään auton kulkemaa matkaa
        self.matka += self.nopeus * aika
        return


'''
    Määritellään Kilpailu-luokka
'''
class Kilpailu:
    def __init__(self, nimi, pituus, kilpailijat):
        self.kilpailun_nimi = nimi
        self.kilpailun_pituus = pituus
        self.kilpailijat = kilpailijat      # lista kilpailijoista

    def tunti_kuluu(self):
        for auto in self.kilpailijat:
            muutos = random.randint(-10, 15)         # arvotaan auton nopeuden muutos
            auto.kiihdyta(muutos)                       # muutetaan auton nopeus
            auto.kulje(1)                               # ajetaan 1h uudella nopeudella

    def tulosta_tilanne(self):
        print("Rekkkari\t huippunopeus\t nopeus\t kuljettu matka")      # \t on tab eli sarkainnäppäin
        # käydään listan kaikki autot läpi
        for kaara in self.kilpailijat:
            # termillä ':15d' numero tulostetaan 15 merkkiä leveään kenttään
            print(f"{kaara.rekisteritunnus:10s} {kaara.huippunopeus:10d} {kaara.nopeus:10d} {kaara.matka:12d}")

    def kilpailu_ohi(self):
        # oleutsvastaus: False eli kilpailu ei ole ohi
        vastaus = False
        # käydään kaikki kilpailijat läpi,  palautetaan True,
        # jos yksikin auto on päässyt maaliin. Muuten False
        for kaara in self.kilpailijat:
            if kaara.matka > 8000:
                vastaus = True
                break               # lopetetaan for-toisto heti, jos jokin autoon päässyt maaliin
        return vastaus


# - pääohjelma
auto1=Sähköauto(52.5, "ABC-15", 180)
auto2=Polttomoottoriauto(32.3,"ACD-123", 165)

auto1.nopeus = 50
auto2.nopeus = 60

auto1.kulje(3)
auto2.kulje(3)

print("Sähköauton matkamittarlukema:",auto1.matka)
print("Polttomoottriauton matkamittarilukema:",auto2.matka)
