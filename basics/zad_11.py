x = int(input('Podaj liczbe x:'))
y = int(input('Podaj liczbe y:'))

if x > 100 or x < 0 or y > 100 or y < 0:
    pozycja = "poza planszą"
elif x >= 10 and x <= 90 and y >= 10 and y <= 90:
        pozycja = "centrum"
elif x < 10 and y < 10:
        pozycja =  "dolnym lewym rog"
elif x < 10 and y > 90:
        pozycja = " gorny lewy rog"
elif x < 10 and y < 90:
        pozycja = " prawa krawedz"
elif x > 90 and y < 10:
        pozycja = " dolny prawy rog"
elif x > 90 and y > 90:
        pozycja = " gorny prawy rog"
elif x > 90 and y < 90:
        pozycja = "lewa krawedz"
elif x > 90 and y < 90:
        pozycja = "gornym krawedz"
elif x > 90 and y < 90:
        pozycja = "dolnej krawedz"
print(f"Twoja pozycja to {pozycja}")