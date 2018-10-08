#program do liczenie koszty za paliwo z miasta A do B

a = input('Podaj miasto A')
b = input('Podaj miasto B')
d = int(input(f'Podaj dystans {a}- {b}'))
cena = float(input('Podaj cenę paliwa'))
spalanie = float(input('Podaj spalanie'))
naleznosc = round((d / 100 * cena * spalanie), 2)


print(f"Miasto A = {a}\n Miasto B = {b}\n Dystans = {d} km\n Cena paliwa: 4.55\n Spalanie na 100 km: 5.5\n\n Koszt przejazdu Warszawa-Gdañsk to {naleznosc} PLN")