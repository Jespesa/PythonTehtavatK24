import random
# määritellään Auto-luokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        # alla olevia ominaisuuksia ei voi asettaa oliota luodessa
        self.nopeus = 0  # tämän hetken nopeus
        self.matka = 0  # auton kulkema matka

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
# luodaan tyhjä lista kilpailijoita varten
kilpailijat = []

# luodaan kilpailevat autot ja lisätään ne listaan
for nro in range(1, 11):
    # määritetään auton ominaisuudet
    rekkari = "ABC-" + str(nro)
    huippunop = random.randint(100, 200)
    # luodaan uusi Auto-luokan olio
    kaara = Auto(rekkari, huippunop)
    # lisätään luotu olio listaan
    kilpailijat.append(kaara)

# luodaan uusi kilpailu
romuralli = Kilpailu("Suuri romuralli", 8000, kilpailijat)
# kuinka monta tutia kilpailu on kestänyt?
kilpailun_kesto = 0
# onko kilpailu loppunut?
kilpailu_paattynyt = False

# toistetaan, kunnes kilpailu päättyy
while kilpailu_paattynyt != True:
    # ajetaan kilpailua tunti lisää
    romuralli.tunti_kuluu()
    # onko joku päässyt maaliin, talletetaan saatu vastaus muuttujaan 'kilpailu_paattynyt'
    kilpailu_paattynyt = romuralli.kilpailu_ohi()
    # lisätään kilpailun kestoa tunnilla
    kilpailun_kesto += 1
    # jos kilpailum kesto on jaollinen 10:lla, niin tulostetaan sen hetkinen tilanne
    if kilpailun_kesto % 10 == 0:
        print(f"Kilpailu on kestänyt {kilpailun_kesto} tuntia, tilanne:")
        romuralli.tulosta_tilanne()

# kilpailu on päättynyt, jos tänne tullaan
print(f"Kilpailu on päättynyt {kilpailun_kesto} tunnin jälkeen")
print("* Alla ovat kilpailun lopputulokset *")
romuralli.tulosta_tilanne()