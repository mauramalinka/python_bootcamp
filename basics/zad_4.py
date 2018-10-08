
a = float(input('Podaj liczbę:'))


print(f"większa od 10 {a>10}")
print(f"Liczba wieksza równa 15: {a%2 == 0}")

print(f"Podzielna przez 2 i wieksza od 10: {a%2 == 0 and a>10}")
print(f"Podzielna przez 3 lub wieksza od 10: {a%3 == 0 or a>10}")