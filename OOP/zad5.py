class CashMachine:

    def __init__(self):
        self.money = []

    def __str__(self):
        return f"{self.money}"

    def is_availabe(self):
        return len(self.money) > 0

    def put_banknot(self, lista = []):
        for banknot in lista:
            self.money.append(banknot)

    def withdraw_money(self, lista):
        lista = self.money
        for banknot in lista:
            self.money.append(banknot)

cash_machine = CashMachine()

cash_machine.is_availabe()


print(f"{cash_machine}")

cash_machine.put_banknot([100, 50, 100, 50])

print(f"{cash_machine}")

print(f"{cash_machine.is_availabe()}")