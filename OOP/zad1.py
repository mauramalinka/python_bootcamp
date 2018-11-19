class Produkt:

    def __init__(self, cena, nazwa, ID):
        self.cena = cena
        self.nazwa = nazwa
        self.ID = ID

    def print_info(self):
        print(f"Produkt: {self.nazwa}, {self.ID}, {self.cena} PLN")

produkt = Produkt(10.99, 'Woda', 1)
#produkt2 = Produkt(5.99, 'Piwo', 2)

produkt.print_info()
#produkt2.print_info()