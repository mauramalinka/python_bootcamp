napis = input("Podaj napis:")

liczniki = {}
l=0

for litera in napis.lower():
    if litera != " ":
        liczniki[litera] = liczniki.get(litera, 0) + 1
#    if litera in liczniki:
#        liczniki[litera] = liczniki[litera] + 1
#    else:
#        liczniki[litera]=1
print(liczniki)