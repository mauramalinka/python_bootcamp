#Napisz program zliczajacy liczbe unikalnych liczb wprowadzonych
#przez uzytkownika. Sprawdz jak duzo z tych liczb jest liczbami
#parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora
#iloczynu.

liczby = input("Podaj liczby: ")
liczby = set(liczby)
parzyste = set(range(2,100,2))
tablica=[]


#print(parzyste)
print(liczby)
#liczby = set(liczby)
print(liczby)

for liczba in liczby:
    if liczba == "k":
        break
    else:
       tablica.append(liczba)
       liczby = input("Podaj liczby: ")
#    elif type(liczba) != int:
#       print(f"Podaj liczby")

tablica =set(tablica)
print(f"{len(tablica)}")
print(tablica)

print(tablica & parzyste)

