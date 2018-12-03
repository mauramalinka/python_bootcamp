lista  = [1, 2, 3, 4]

try:
    print(lista[5])
    lista.add(5)
except IndexError as e:
     raise IndexError("Próbujesz pobrać jakiś element spoza zakresu listy")
except AttributeError as e:
    print("Prawdopodobnie wywołujesz metodę, której ten obiekt nie ma")

print("aAAA")