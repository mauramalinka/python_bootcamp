class Przedmiot:

    def __init__(self, nazwa, bonus):
        self.nazwa = nazwa
        self.bonus = bonus

    def pokaz_przedmiot(self):
        print("Mam {self.nazwa}, co daje {self.bonus}")

