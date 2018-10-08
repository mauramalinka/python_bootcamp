a = float(input('Podaj liczbę:'))

wynik = a == 7 or (
        a % 2 == 0 and
        a % 3 == 0 and
        a > 10
)

print(f"Liczba jest podzielna przez 2 i 3, większa od 10 lub równa 7: {wynik}")
