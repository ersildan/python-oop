class ElectricCar:
    def __init__(self, color):
        self._color = color
    def get_color(self):
        return self._color
    color = property(fget=get_color)

car = ElectricCar('black')
car.color = 'yellow'
print(car.color)