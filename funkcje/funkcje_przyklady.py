def dodaj(a,b):
    return a + b

def test_dodaj():
    assert dodaj(1,2) == 3

# def test_dodaj():
#     assert dodaj(1,2) == 4

def test_dodaj_dwa_napisy():
    assert dodaj("1","2") == "12"