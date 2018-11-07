data = [1, 2, 3, 4, 5, 6, 7]


def bigger_than_3(liczba):
    if liczba > 3:
        return True
    return False


def sprawdzam_czy_wieksze_3(lista):
    out = []
    for element in lista:
        out.append(bigger_than_3(element))
    return out


def sprawdzam_czy(lista, start, stop):
    out = []
    for element in lista:
        out.append(warunek(element))
    return out


assert sprawdzam_czy(lista, bigger_than_3) == out
assert sprawdzam_czy(lista, lambda i: i == 4) == [False, False, False, True, False, False]
# def sprawdzam_czy_wieksze_3:
#    out = []
#    for element in lista:
#        if element > 3:
#            out.append(True)
#        else:
#            out.append(False)
#    return out
