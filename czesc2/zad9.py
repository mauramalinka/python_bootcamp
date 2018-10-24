slownik = {"woda":2, "ziemniaki":3.5, "pomidory":20}
total = 0

koszyk = {}

magazyn  = {"woda":10, "ziemniaki":10, "pomidory":10}

while True:
    komenda = input("""Wybierz opcje: 
               [d] - dodaj do magazynu
               [k] - kup
               [z] - zakoncz""")
    if komenda == "k":
        print(f" W naszym sklepie oferujemy:")
        for x in slownik:
            print(f" - {x} - w cenie: {slownik[x]} PLN")
        produkty = input("Podaj produkty jakie chcesz kupić: woda, ziemniaki czy pomidory: ")
        if produkty == "Koniec":
            break
        if produkty in slownik:
            x = int(input("Podaj ich mase: "))
            if x <= magazyn[produkty]:
            #cena = slownik[produkty] * x
            koszyk[produkty] = x
            magazyn[produkty] -= x
         else:
            print(f"Brak produktu [magazyn{produkty}]")
        print()

        for produkty in koszyk:
            print(f"Twój rachunek - {produkty}: koszyk[produkty]")
            cena = koszyk[produkty] * slownik[produkty]
            total += cena
            print(f"{total}")
            print("Zapraszamy ponownie")

    elif komenda == "d"
        co = input(f"Podaj")
        ile = int(input(f"ile"))
        magazyn[co] = magazyn.get(co,0) + x
        if co not in slownik:
            cena = float(input(f'Jaka cena za {co}'))
            produkty[co] = x
    elif komenda = "z":
        print(f"Koniec")