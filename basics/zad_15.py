from random import randint

graceX = randint(1, 10)
graceY = randint(1, 10)
i = 0

print(f"Skarb jest: {graceX, graceY}")

#graceX = 5
#graceY = 5

youX = randint(1, 10)
youY = randint(1, 10)

print(f"Twoje położenie to: {youX, youY}")


while True:

    ruch = input(f"Jaki chcesz ruch wykonać: g, d, p LUB l")
    i +=1
    minKROKOWprzed = abs(youX - graceX) + abs(youY - graceY)

    if ruch == "g":
        youY = youY + 1
    elif ruch == "d":
        youY = youY - 1
    elif ruch == "p":
        youX = youX + 1
    elif ruch == "l":
        youX = youX - 1

    print(f"Twoje położenie to: {youX, youY}")
    minKROKOWpo = abs(youX - graceX) + abs(youY - graceY)

    if minKROKOWpo == 0:
        print(f"BRAWO! Znalazłeś skarb w {i} kroków")
        break
    elif minKROKOWpo < minKROKOWprzed:
        print(f"zblizasz sie")
    else:
        print(f"oddalasz sie")


    if youX == graceX and youY == graceY:
        print(f"BRAWO! Znalazłeś skarb w {i} kroków")
        break
    if abs(youX - graceX) <= 1 and abs(youY - graceY) <= 1:
        print(f"jestes blisko")
    elif youX < 1 or youX > 10 or youY < 1 or youY > 10:
        print(f"jestes poza plansza. Przegraeles")
        break





