#program do liczenia objętości pudła i sprawdzić czy jest większa od 1 litra
a = float(input('Podaj wymiar podstawy a w cm'))
b = float(input('Podaj wymiar podstawy b w cm'))
h = float(input('Podaj wymiar wysokości h w cm'))

V = a * b * h

print(f"Objęstość pudła jest: {V} cm3 i jest większa od 1 litra: {V>1000}")

if V > 2000:
    print(f"Objętość większa niż 2l")
elif  V > 1000:
    print(f"Objętość większa niż 1l")
else:
    print(f"Objętość mniejsza lub równa 1l")

a = 0

if a:
    print(f"Sprawdzenie a")