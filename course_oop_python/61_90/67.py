from functools import singledispatchmethod

class ElectricCar:

    @singledispatchmethod
    def __init__(self, color):
        self.color = color

    @__init__.register(list)
    def _(self, color):
        self.color = ', '.join(color)

car1 = ElectricCar('yellow')
car2 = ElectricCar(['black', 'white'])

print(car1.color)
print(car2.color)