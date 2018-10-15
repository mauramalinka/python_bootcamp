znalezione_max = None
znalezione_min = None


while True:
    dane = input('Podaj liczby n lub k by zakończyć:')

    if (dane == "k"):
        break

    x = int(dane)
    if znalezione_max is None or x > znalezione_max:
        znalezione_max = x
    if znalezione_min is None or x < znalezione_min:
        znalezione_min = x

if znalezione_max is None:
    print(f"Nie wprowadziles danych")
else:
    print(f"max i min = {znalezione_max} i {znalezione_min}")
