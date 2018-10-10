a = input('Podaj liczbe a:')
b = input('Podaj liczbe b:')


if a.isnumeric() and b.isnumeric():
    a = int(a)
    b = int(b)
    c = input('Podaj rodzaj operacji (+, -, *, /):')

    if c == "+":
        print(f"Suma = {a + b}")
    elif c == "-":
        print(f"Roznica = {a - b}")
    elif c == "*":
        print(f"Iloczyn = {a * b}")
    elif c == "/":
        if b == 0:
            print(f"Nie dziel przez 0")
        else:
            print(f"Iloraz = {a / b}")
    else:
        print(f"Nie rozumiem operacji dzialania")

else:
    print(f"Podaj tylko liczby")
# mozna usunac te printy, najpierw policzyc i dopiero na koncu print