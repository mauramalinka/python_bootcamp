class ElectricCar():

    def __init__(self, max_zasieg):
        self.zasieg = max_zasieg
        self.max_zasieg = max_zasieg

    def drive(self, dystans):
        if dystans > self.zasieg:
            wynik = self.dystans
            self.range = 0
            return wynik
        else:
            self.dystanse -= dystans
        return dystans

    def charge(self):
        self.zasieg = self.max_zasieg

car = ElectricCar(100)
print(car.drive(70))
print(car.drive(50))
print(car.drive(20))
