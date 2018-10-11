dane = 0
i = 0
x= 0
while True:
    dane = input('Podaj temperature T lub wpisz k to zakonczy:')
    if dane != "k":
        dane = float(dane)
        x += dane
        i += 1
        srednia = x / i
    else:
        break
print(f"Srednia T = {srednia}")

