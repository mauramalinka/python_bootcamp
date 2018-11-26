class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

class Employee(Osoba):

    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko) #trzeba dodac aby zmienic jakies metody
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

class PremiumEmployee(Employee):

    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka) #trzeba dodac aby zmienic jakies metody
        self.bonus = 0

    def give_bonus(self, kwota):
        self.bonus += kwota

    def pay_salary(self):
        self.bonus = 0
        to_pay = super().pay_salary() + self.bonus
        return to_pay

employee = PremiumEmployee("Jan", 'Nowak', 100.0)



employee.register_time(5)
print(employee.pay_salary())
employee.register_time(0)
print(employee.pay_salary())
employee.register_time(10)
print(employee.pay_salary())