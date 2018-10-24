slownik = {"woda":2, "ziemniaki":3.5, "pomidory":20}

print(f" W naszym sklepie oferujemy:")
for x in slownik:
    print(f" - {x} - w cenie: {slownik[x]} PLN")

print()
wybor_produktu = input("Który produkt")

produkty = input("Czy cos jeszcze: woda, ziemniaki czy pomidory: ")
y  = int(input("Podaj ich mase: "))

for k in slownik:
    if k == produkty:
        print({slownik[k] * y})

produkty = input("Czy cos jeszcze: woda, ziemniaki czy pomidory: ")
z  = int(input("Podaj ich mase: "))

for k in slownik:
    if k == produkty:
        print({slownik[k] * z})

print(f"Zaplac: {slownik[k] * x} + {slownik[k] * y} + {slownik[k] * z}" )