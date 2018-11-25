#program do tworzenie postaci i walki

from random import randint
from przedmiot import Przedmiot

# randint(1,10)

class Postac:

    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self.atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []

    def przedstaw_sie(self):
        print(f"Nazywam się: {self.imie}, mam ataku : {self.atak} i  {self.zdrowie}/{self.max_zdrowie} życia")

    def walka(self, ile):
        self.zdrowie = self.zdrowie - ile
        if self.zdrowie < 0:
            print(f"{self.imie} umarłem")
            self.zdrowie = 0

    def leczenie(self, lek):
        if self.zdrowie <= 0:
            print(f"Nie można leczyć nieboszczyka")
        elif self.zdrowie + lek < self.max_zdrowie:
            self.zdrowie = self.zdrowie + lek
        else:
            self.zdrowie = self.max_zdrowie

    def __str__(self):
        return f"Nazywam się: {self.imie}, mam ataku : {self.atak} i  {self.zdrowie}/{self.max_zdrowie} życia i mam {self.ekwipunek}"

    def moc_ataku(self):
        return randint(self.atak // 2, self.atak)

    def atak_plus(self):
        wynik = self.atak
        for przedmiot in self.ekwipunek:
            wynik += przedmiot.bonus
            return wynik

    @staticmethod
    def fight(atakujacy, broniacy):
        while atakujacy.zdrowie > 0 and broniacy.zdrowie > 0:
            print(atakujacy)
            print(broniacy)
            atakujacy_atak = atakujacy.moc_ataku()
            broniacy_atak = broniacy.moc_ataku()
            print(f"Walka: {atakujacy.imie} vs {broniacy.imie}")
            broniacy.walka(atakujacy_atak)
            print(f"{atakujacy.imie} przyłożył {broniacy.imie} za {atakujacy_atak}")
            atakujacy.walka(broniacy_atak)
            print(f"{broniacy.imie} przyłożył {atakujacy.imie} za {broniacy_atak}")
        print(f"Koniec walki")


    def daj_przedmiot(self, przedmiot):
        return self.ekwipunek.append

rufus = Postac("Rufus", 30, 100)
#rufus.walka(90)
#print(rufus)
#rufus.leczenie(10)
#print(rufus)
#rufus.walka(20)
#rufus.leczenie(10)
#rufus.leczenie(10)
#print(rufus)

janina = Postac("Janina", 20, 400)

tulipan = Przedmiot("Zielony tulipan zniszczenia", 5)
rufus.daj_przedmiot(tulipan)
rufus.atak_plus()

print(f"{rufus.atak_plus()}")
Postac.fight(rufus, janina)



def test_obrazenia():
    postac = Postac("Rafał", 5, 200)
    assert postac.zdrowie == 200
    postac.walka(80)
    assert postac.zdrowie == 120
    postac.walka(120)
    assert postac.zdrowie == 0

def test_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.leczenie(20)
    assert postac.zdrowie == 200
    postac.walka(100)
    assert postac.zdrowie == 100