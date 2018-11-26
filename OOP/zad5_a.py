class CashMachine:

    def __init__(self):
        self._money = []

    @property
    def is_avaiable(self):
        if self._money:
            return True
        return False

    def put_money(self, money):
        self._money.extend(money)

    def withdraw_money(self, kwota):
        wallet_temp = []
        for bill in sorted(self._money, reverse=True):
             if sum(wallet_temp) + bill <= kwota:
                 wallet_temp.append(bill)
        if sum(wallet_temp) != kwota:
            return []
        for bill in wallet_temp:
            self._money.remove(bill)
        return wallet_temp

def test_cash_machine_not_avaiable():
    cash_machine = CashMachine()
    assert not cash_machine.is_avaiable


def test_cash_machine_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([50])
    cash_machine.put_money([50])
    assert cash_machine.is_avaiable

def test_cash_machine_whithdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    wallet = cash_machine.withdraw_money(150)
    assert wallet == [100, 50]
    wallet = cash_machine.withdraw_money(150)
    assert wallet == []

def test_cash_machine_whithdraw_money_sort():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 20, 50])
    wallet = cash_machine.withdraw_money(150)
    assert wallet == [100, 50]
