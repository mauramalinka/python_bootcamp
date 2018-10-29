def czy_pierwsza(x):
    for y in range(2, x - 1):
        if x % y == 0:
            return False
    return True


def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_pierwsza(11)
    assert czy_pierwsza(3)
    assert czy_pierwsza(101)

def test_czy_jest_pierwsza_dla_liczby_nie_pierwszej():
    assert not czy_pierwsza(10)
    assert not czy_pierwsza(55)
    assert not czy_pierwsza(161)

