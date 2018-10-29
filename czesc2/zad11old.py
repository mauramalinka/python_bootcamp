zbior_a = set()

while True:
    a = input("Podaj liczb")
    if a == "k":
        break
    else:
        a = int(a)
        zbior_a.add(a)
zbior_b = set(range(2, 100, 2))

print(f"Ilość liczb:{len(zbior_a)}")
print(f" Cześć wspólna: {zbior_a & zbior_b}")