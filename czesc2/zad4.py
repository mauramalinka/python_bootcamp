ilosc = 0
for x in range(101):
    if x % 3 == 0 or x % 5 == 0:
        print(x)
        ilosc += 1

print(f"ilosc liczb podzielnych przez 3 i 5 w zakresie od 0 do 100 jest równa: {ilosc}")

