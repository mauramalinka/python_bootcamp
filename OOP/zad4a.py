class Produkt:

    def __init__(self, cena, nazwa, ID):
        self.cena = cena
        self.nazwa = nazwa
        self.ID = ID

    def print_info(self):
        print(f"Produkt: {self.nazwa}, {self.ID}, {self.cena} PLN")

produkt = Produkt(10.99, 'Woda', 1)
produkt2 = Produkt(5.99, 'Piwo', 2)

produkt.print_info()
produkt2.print_info()

class BasketEntry:

    def __init__(self, produkt, quantity):
        self.produkt = produkt
        self.quantity = quantity

    def count_price(self):


class Basket:

    def __init__(self):
        self.basket = []

    def add_produkt(self, n):
        self.basket.append(BasketEntry(produkt, qty))

    def count_total_price(self):
        price = 0
        price = self.cena * self.n

    def generate_report():
        print(f"Produkty w koszyku: \n - {self.name}, cena: {self.cena} x {self.n}\n W sumie: {price}")


basket.add_produkt('Sok', 5)

basket.generate_report()