
i= 0
lista = []
while len(lista) < 10:

    x = input('Podaj liczby lub k by zakonczyć:')

    if x == "k":
        break
    liczba = int(x)
    lista.append(liczba)

if len(lista) == 0:
    print(f"nie umiem dzielic przez 0")
else:
    srednia = sum(lista)/len(lista)
    print(f"{srednia}")