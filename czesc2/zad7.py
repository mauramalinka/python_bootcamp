napis = input("Podaj napis: ")
i = 0
licznik = 0

for litera in napis:
    if litera == "a" or litera == "A":
        i += 1
    if litera == "e" or litera == "E":
        i += 1
    if litera == "i" or litera == "I":
        i += 1
    if litera == "o" or litera == "O":
        i += 1
    if litera == "u" or litera == "U":
        i += 1
    if litera == "y" or litera == "Y":
        i += 1
print(f"{i}")

# lepsze rozwiązanie

SAMOGLOSKI = "aeiouy"

for litera in napis.lower():
    if litera in SAMOGLOSKI:
        licznik += 1

print(f"{licznik}")
#print(napis[0])Pada
#print("D" in napis)
#print("d" in napis)

