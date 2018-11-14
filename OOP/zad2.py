class Employee():

    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.time = 0

    def register_time(self, time):
        self.time += time

    def pay_salary(self):
        if self.time <= 8:
            salary = self.time * self.stawka
            self.time = 0.0
        if self.time > 8:
            salary = self.time * self.stawka + (self.time - 8 ) * self.stawka
            self.time = 0.0
        return salary


employee = Employee("Jan", 'Nowak', 100.0)


employee.register_time(5)
print(employee.pay_salary())
employee.register_time(0)
print(employee.pay_salary())
employee.register_time(10)
print(employee.pay_salary())