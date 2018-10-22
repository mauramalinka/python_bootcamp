slownik= {}
slownik = dict()

print(type(slownik))

slownik["klucz"] = "wartosc"

#klucz nie może byc lista
# klucze są unikalne


slownik["lista"] = [1,2,3]

slownik["jeden"] = [1]

slownik2 = {"a":1, "b":2}

print(slownik["jeden"])
print(slownik)
print(slownik2)

dir(slownik2)
print(slownik2.items())
print(slownik2.values())

for k in slownik2:
    print(k, slownik2[k])