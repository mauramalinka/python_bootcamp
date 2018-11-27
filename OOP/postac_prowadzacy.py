from random import randint
from przedmiot import Przedmiot

# randint(1, 10) - losowa liczba całkowita z przedziału 1-10

class Postac():
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []

    @property
    def atak(self):
        wynik = self._atak
        for p in self.ekwipunek:
            wynik += p.bonus_atk
        return wynik

    def __str__(self):
        if self.czy_zyje():
            napis = "EKWPIUNEK:\n"
            for x in self.ekwipunek:
                napis += str(x) + "\n"
            return f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.\n" + napis
        else:
            return f"Jestem {self.imie}, miałem {self.atak} ataku i nie żyję."

    def wylecz(self, ile):
        if self.czy_zyje():
            print(f"{self.imie} został ulaczony za {ile} punktów życia.")
            self.zdrowie = self.zdrowie + ile
            if self.zdrowie > self.max_zdrowie:
                self.zdrowie = self.max_zdrowie
        else:
            print(f"Próbujesz wyleczyć trupa.")

    def otrzymaj_obrazenia(self, ile):
        print(f"{self.imie} oberwał za {ile} obrażeń.")
        self.zdrowie = self.zdrowie - ile
        if self.zdrowie < 0:
            self.zdrowie = 0

    def czy_zyje(self):
        return self.zdrowie > 0

    def moc_ataku(self):
        wynik = randint(self.atak // 2, self.atak)
        return wynik

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def atak_plus(self):
        wynik = self.atak
        for przedmiot in self.ekwipunek:
            wynik += przedmiot.bonus_atk
            return wynik

    @staticmethod
    def walka(atakujacy, broniacy):
        print(f"Walka: {atakujacy.imie} vs {broniacy.imie}")
        while atakujacy.czy_zyje() and broniacy.czy_zyje():
            print(atakujacy)
            print(broniacy)
            atak_atakujacego = atakujacy.moc_ataku()
            atak_broniacego = broniacy.moc_ataku()
            print(f"{atakujacy.imie} uderza {broniacy.imie} za {atak_atakujacego} obrażeń.")
            broniacy.otrzymaj_obrazenia(atak_atakujacego)
            print(f"{broniacy.imie} uderza {atakujacy.imie} za {atak_broniacego} obrażeń.")
            atakujacy.otrzymaj_obrazenia(atak_broniacego)
        print("KONIEC WALKI")

rufus = Postac("Rufus", 30, 105)
janusz = Postac("Janusz", 40, 120)

tulipan = Przedmiot("Zielony tuplian zniszczenia", 5)
rufus.daj_przedmiot(tulipan)
print(f"{rufus.atak_plus()}")
Postac.walka(rufus, janusz)

jola = Postac("Jola", 25, 1000)
zocha = Postac("Zocha", 27, 1500)

kryształ = Przedmiot("Błękitny kryształ", 500)
jola.daj_przedmiot(kryształ)
Postac.walka(jola, zocha)

def test_nowa_postac():
    postac = Postac("Albert", 1, 20)
    assert postac.imie == "Albert" and postac.atak == 1 and postac.zdrowie == 20 and postac.max_zdrowie == 20

def test_obrazenia():
    postac = Postac("Rafał", 5, 200)
    assert postac.zdrowie == 200
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.otrzymaj_obrazenia(200)
    assert postac.zdrowie == 0

def test_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(50)
    assert postac.zdrowie == 170

def test_leczenie_nieboszczyka():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(800)
    assert postac.zdrowie == 0
    postac.wylecz(50)
    assert postac.zdrowie == 0

def test_za_duze_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(500)
    assert postac.zdrowie == 200