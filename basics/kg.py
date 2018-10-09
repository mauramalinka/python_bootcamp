#program do liczenie ceny zakupu

cena = float(input('Podaj cenę za kg w PLN'))
waga = float(input('Podaj masę w kg'))

naleznosc = cena * waga

print(f"Cena za kg w PLN = {cena}\n waga w kg ={waga}\n należność = {naleznosc} PLN")