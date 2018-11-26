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

v1 = Vector(1,3)
v2 = Vector(4,4)

print(v1)
print(v2)
v3 = v1 + v2
print(v3)

v2 += v1
print(v2)