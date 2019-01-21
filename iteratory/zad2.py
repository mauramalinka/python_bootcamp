



class Vowels():

    def __init__(self, napis):
        self.napis = napis

    def __iter__(self):
        self.pozycja = 0
        return self

    def __next__(self):
        while self.pozycja < len(self.napis):
            self.pozycja += 1
            litera = self.napis[self.pozycja]
            if litera  in "aeiouy":
                return litera
        raise StopIteration




for char in Vowels("ala ma kota a kot ma ale"):
    print(char)