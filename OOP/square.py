class Square:

    def __init__(self,a):
        self.a = a
        self.field = self.a ** 2

    def __add__(self, other):
       return self.field + other.field


sq1=Square(2)
sq2=Square(3)

print(sq1 + sq2)

assert sq1.field + sq2.field == 13