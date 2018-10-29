lista = [5, 4, 3, 1, 2]

print("Listy przed:", lista)

for indeks_podsawienia in range(len(lista)):
    indeks_min = indeks_podsawienia
    for indeks_ogona in range(indeks_podsawienia+1, len(lista)):
        if lista[indeks_ogona] < lista[indeks_min]:
            indeks_min = indeks_ogona
    #value_temp = lista[indeks_min]
    #lista[indeks_min] = lista[indeks_podsawienia]
    #lista[indeks_podsawienia] = value_temp
    # poniżej

lista[indeks_min], lista[indeks_podsawienia] = lista[indeks_podsawienia], lista[indeks_min]

print(f"Liczby po:", lista)
assert [1, 2, 3, 4, 5]