class Iterator:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.licznik = 0
        return self

    def __next__(self):
        if self.licznik > self.max:
            raise StopIteration
        liczba = self.licznik
        self.licznik += 1
        return liczba

for i in Iterator(1000):
    print(i)