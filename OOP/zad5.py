class CashMachine:

    def __init__(self):
        self._money = []

    @property
    def is_availabe(self):
        if self.money:
            return True
        return False

    def put_banknot(self, money):
        self._money.extend(money)

    def withdraw_money(self, kwota):
        self.money.sort
        for x in self.money:
             if x <= kwota:
                 return x




cash_machine = CashMachine()

cash_machine.is_availabe()

print(f"{cash_machine}")

cash_machine.put_banknot([100, 50, 100, 50])

print(f"{cash_machine}")

print(f"{cash_machine.is_availabe()}")

cash_machine.withdraw_money(100)

print(f"--------------")
print(f"{cash_machine}")
