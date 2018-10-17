dane = 0
i = 0
x= 0
while True:
    dane = input('Podaj temperature T lub wpisz k by zakonczy:')
    if dane == "k":
        break
    if dane != "k":
        dane = float(dane)
        x += dane
        i += 1
        srednia = x / i

print(f"Srednia T = {srednia}")

