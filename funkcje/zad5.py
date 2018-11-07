liczba = 10

def silnia(liczba):
    if liczba == 0:
        return 1
    else:
        return liczba * silnia(liczba - 1)

def test_silna_dla_5():
    assert silnia(5) == 120
    assert silnia(0) == 1
    