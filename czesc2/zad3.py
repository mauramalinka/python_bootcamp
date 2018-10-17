lista = [1, 4, -5, 9, 0, 3, 9, 1, 5, 9, 10, -3]
plus = 0
minus = 0

for x in lista:
    if x >= 0:
        plus += 1
    elif x < 0:
        minus += 1

print(f"ilosc wartosci dodatnich: {plus} i ujemnych: {minus}")