zbior_a = set()

while True:
    a = input("Podaj liczb")
    if type(a) == class(int):
        zbior_a.add(a)
    else:
        break
zbior_b = set(range(2, 100, 2))

print(len(zbior_a))