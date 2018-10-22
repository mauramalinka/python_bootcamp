napis = input("Podaj napis z jednym nawiasem <>: ")

for litera in napis:
    if litera == "<":
#        print(napis.index(litera))
        x = napis.index(litera)
    elif litera == ">":
        y = napis.index(litera)

print(f" Ilość znaków w nawiasie wynosi: {y - x - 1}")


# inne rozwiazanie
licznik = 0
czy_zliczac = False

for i in napis:
    if i == "<":
        czy_zliczac = True
    elif i == ">":
        czy_zliczac = False
    elif czy_zliczac:
        licznik += 1

print(f" Ilość znaków w nawiasie wynosi: {licznik}")