def wiecej_niz(tekst, i):
    wynik = set()
    for litera in tekst:
        if tekst.count(litera) > i:
            wynik.add(litera)
    return wynik

def test_dla_pustego_napisu():
    assert wiecej_niz("",0) == set()

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("aaa bb cc", 2) == {"a"}
    assert wiecej_niz("aaaa mmmm bbbb llll", 3) == {"a", "m", "b", "l"}