def policz_znaki(tekst, start="<", end=">"):
    return tekst.count(tekst)

def test_pilicz_znaki_bez_znacznikow():
    assert policz_znaki("ala ma kota") == 0

def test_pilicz_znaki_jeden_poziom_znacznikow():
    assert policz_znaki("ala ma <kota>") == 4

def test_pilicz_nie_standardoweznacznik_znacznikow():
    assert policz_znaki("ala [kota [a kot]] ma ale[ale]", start="[", end="]") == 18

def test_pilicz_nie_standardoweznacznik_znacznikow():
    assert policz_znaki("a <a<a<a>>>") == 6