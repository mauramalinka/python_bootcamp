class ElectricCar():

    def __init__(self, max_zasieg):
        self.zasieg = max_zasieg
        self.max_zasieg = max_zasieg

    def drive(self, dystans):
        self.dystans = dystans
        if self.dystans > self.zasieg:
            wynik = self.dystans
            self.zasieg = 0
            return wynik
        else:
            self.dystans -= self.dystans
            return dystans

    def charge(self):
        self.zasieg = self.max_zasieg

car = ElectricCar(100)
print(car.drive(70))
print(car.drive(50))
print(car.drive(50))
