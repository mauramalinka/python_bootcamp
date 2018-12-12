import json
import sys



try:
    with open('emplo.json', "r") as f:
        emplo = json.load(f)
except FileNotFoundError:
    emplo = []
do = input('Co chcesz zrobic: wybierz opcje dodaj - [d], wypisz - [w]')

# class Pracownik():
#     def __init__(self, imie, atak, zdrowie):
#         self.imie = imie
#         self.wiek = wiek
#         self.pensja = pensja


if do == "d":
    imie = input('Podaj Imie')
    wiek = int(input('Podaj wiek'))
    pensja = float(input('Podaj pensje'))
    rok_ur = int(input('Podaj rok ur'))
    emplo.append({"imie" : imie, "wiek": wiek, "pensja": pensja})
    with open("emplo.json", "w") as file:
        json.dump(emplo, file)

elif do == "w":
    for nr, p in enumerate(emplo, 1):
        print(f" - [{nr}] {p['imie']} {p['wiek']} {p['rok_ur']} {p['pensja']} PLN")

