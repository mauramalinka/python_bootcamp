dane = 0
i = 0
while True:
    dane = int(input('Podaj temperature T lub wpisz k to zakonczy:'))
    if T == "k":
        break
    srednia += float(dane)
    i += 1
    print(f"Srednia T:= {srednia/i+1}")

