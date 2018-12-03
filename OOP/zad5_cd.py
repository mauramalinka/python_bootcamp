import pytest


class NoEnoughMoney(ValueError):
    pass


class AmountNotDividedBy10(ValueError):
    pass


class CashMachine:

    def __init__(self):
        self._money = []

    @property
    def is_avaiable(self):
        if self._money:
            return True
        return False

    def put_money(self, money):
        if len(money) + len(self._money) > 10:
            raise ValueError("Za dużo kaski chcesz wpłacić koleżko")
        self._money.extend(money)

    def whitdraw_money(self, to_withdraw):

        if to_withdraw % 10 != 0:
            raise AmountNotDividedBy10("BŁAD: Kwota powinna być wielokrotnością 10!")

        bills_to_withdraw = []
        for bill in sorted(self._money, reverse=True):
            if sum(bills_to_withdraw) + bill <= to_withdraw:
                bills_to_withdraw.append(bill)

        if sum(bills_to_withdraw) != to_withdraw:
            raise NoEnoughMoney("BŁAD: brak wystarczajacej liczby banknotów dla kwoty 150!")

        for bill in bills_to_withdraw:
            self._money.remove(bill)

        return bills_to_withdraw

    @property
    def empty_slots(self):
        return 10 - len(self._money)

    def __str__(self):
        return f"Bankomat zawiera {self.empty_slots} pustych miejsc na banknoty"

def main():
    bankomat = CashMachine()
    while True:
        operacja = input("Podaj typ operacji w - wpłata, y - wypłata, k - zakończ: ")
        if operacja == 'k':
            print("Dziękujemy za skorzystanie z naszych usług")
            return None
        if operacja == "0123":
            print(bankomat)
        # wpłata
        if operacja == 'w':
            banknoty = input("Podaj jakie banknoty wpłacasz - wpisz je rozdzielając spacją: ")
            banknoty = banknoty.split()
            banknoty = [int(x) for x in banknoty]
            try:
                bankomat.put_money(banknoty)
            except ValueError as e:
                print(e)

        # wypłata
        if operacja == "y":
            kwota_do_wyplaty = int(input("Jaką kwotę chcesz wypłacić: "))
            try:
                wyplacone = bankomat.whitdraw_money(kwota_do_wyplaty)
            except ValueError as e:
                print("Wpadłem tu")
                wyplacone = False
                print(e)

            if wyplacone:
                print(wyplacone)

main()


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
    wallet = cash_machine.whitdraw_money(150)
    assert wallet == [100, 50]
    with pytest.raises(NoEnoughMoney):
        cash_machine.whitdraw_money(150)


def test_cash_machine_whithdraw_money_sort_is_important():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 20, 50])
    wallet = cash_machine.whitdraw_money(150)
    assert wallet == [100, 50]


def test_cash_machine_whithdraw_money_value_is_not_divided_by_ten():
    cash_machine = CashMachine()
    with pytest.raises(AmountNotDividedBy10) as e:
        cash_machine.whitdraw_money(123)