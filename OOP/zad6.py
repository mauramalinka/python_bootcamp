class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Wektor: {self.x}, {self.y}"

    def __add__(self, other):
        nowy_x = self.x + other.x
        nowy_y = self.y + other.y
        return Vector(nowy_x, nowy_y)

    def __sub__(self, other):
        nowy_x = self.x - other.x
        nowy_y = self.y - other.y
        return Vector(nowy_x, nowy_y)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            nowy_x = other * self.x
            nowy_y = other * self.y
            return Vector(nowy_x, nowy_y)
        if isinstance(other, Vector):
            skalar = self.x * other.x + self.y * other.y
            return skalar

    def __truediv__(self, liczba):
            nowy_x = self.x / liczba
            nowy_y = self.y / liczba
            return Vector(nowy_x, nowy_y)

    def dlugosc_vector(self):
        d = (self.x ** 2 + self.y ** 2) ** (1 / 2)
        return f"Vector ({self.x}, {self.y}) has length:{d}"

    def __lt__(self, other):
        d1 = self.dlugosc_vector()
        d2 = other.dlugosc_vector()
        return d1 < d2


v1 = Vector(1, 3)
v2 = Vector(4, 4)

print(v1)
print(v2)
print(f"-----dodawanie-------")
v3 = v1 + v2
print(v3)

print(f"------odejmowanie---------")
v4 = v1 - v2
print(v4)

print(f"------mnozenie przez liczbe---------")

v5 = v1 * 10
print(v5)

print(f"------mnozenie skalarne---------")

v10 = v1 * v2
print(v10)

print(f"--------dlugosc-------")
v4.dlugosc_vector()
print(f"{v4.dlugosc_vector()}")

print(f"------porownanie-------")

v6 = Vector(0, 0)
v7 = Vector(1, 1)

print(v6 < v7)

print(f"------porownanie2-------")

v8 = Vector(10, 20)
v9 = Vector(8, 13)
print(v8 > v9)

print(f"------dzielenie-------")

print(v8 / 2)