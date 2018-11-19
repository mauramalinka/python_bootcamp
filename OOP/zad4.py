from zad1 import Produkt

class Basket():

    def add_produkt(self, produkt, n):
        koszyk = []
        koszyk.append(produkt)
        self.n = n

    def count_total_price(self, price):
        self.price = self.cena * self.n

    def generate_report(self):
        print(f"Produkty w koszyku: \n - {self.nazwa}, cena: {self.cena} x {self.n}\n W sumie: {price}")

basket = Basket()

produkt = Produkt(10.99, 'Woda', 1)

basket.add_produkt(produkt, 5)

print(f"{basket.add_produkt(produkt, 5)}")

print(f"{basket}")

print(basket.generate_report())



