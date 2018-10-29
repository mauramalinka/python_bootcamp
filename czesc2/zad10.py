napis = input("Podaj napis: ").lower()
liczniki = {}
print(liczniki)
for litera in napis:
    if litera != " ":
        liczniki[litera] = liczniki.get(litera, 0) + 1
    # if litera in liczniki:
    #     liczniki[litera] = liczniki[litera] + 1
    # else:
    #     liczniki[litera] = 1

# print(litera)
# print(dir(napis))

print(liczniki)