# 1. Robimy zakupy w pętli. Po wpisaniu zakończ program powinien się zakończyć
# 2. "Sorry nie mam tego produktu"
# 2a. Dodajemy produkty do koszyka i po zakończeniu zakupów drukujemy paragn
# 3. Wprowadzimy magazyn przechowujacy ilosc produktu. "Sorry nie mam tyle tego produktu"
# 4. Dodanie produktu do sklepu


produkty = {
    "ziemniaki": 3,
    "cebula": 2,
    "woda": 1.5,
    "piwo": 2.5
}

magazyn = {
    "ziemniaki": 10,
    "cebula": 10,
    "woda": 10,
    "piwo": 10
}

koszyk = {}



while True:
    komenda = input("""Wybierz opcję: 
    [d] - dodaj do magazynu
    [k] - kup
    [z] - zakończ
    """)
    if komenda == 'k':
        print("W naszym sklepie oferujemy: ")
        for produkt in produkty:
            print(f" - {produkt} - w cenie: {produkty[produkt]} PLN")

        print()
        wybor_produktu = input("Który produkt chcesz kupić? (wpisz koniec by zakończyć zakupy)")
        if wybor_produktu == "koniec":
            break
        if wybor_produktu in produkty:
            ile = int(input(f"Ile chcesz kupić [{wybor_produktu}]: "))
            if ile <= magazyn[wybor_produktu]:
                koszyk[wybor_produktu] = ile
                magazyn[wybor_produktu] -= ile
                # magazyn[wybor_produktu] = magazyn[wybor_produktu] - ile
            else:
                print(f"Przykro mi. Nie mam tyle tego produktu! Pozostało [{magazyn[wybor_produktu]}]")
        else:
            print("Sorry nie mam tego produktu")
        print()
        print("-"*40)
    elif komenda == 'd':
        co = input("Jaki produkt chcesz dodać? ")
        ile = int(input(f"Ile {co} chcesz dodać?"))
        magazyn[co] = magazyn.get(co, 0) + ile
        if co not in produkty:
            cena = float(input(f"Jaka cena za {co}"))
            produkty[co] = cena
    elif komenda == 'z':
        break

print()
print()
print("Twój rachunek: ")
sumarycznie = 0
for produkt in koszyk:
    cena = koszyk[produkt] * produkty[produkt]
    print(f" - {produkt} [{koszyk[produkt]}]: {cena} PLN")
    sumarycznie += cena
print("="*30)
print(f"Suma: {sumarycznie} PLN")

print("Dziękujemy! Zapraszamy ponownie!")