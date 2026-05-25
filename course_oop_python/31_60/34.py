class ElectricCar:
    def __init__(self, color):
        self._color = color
    def get_color(self):
        return self._color
    color = property()

car = ElectricCar('black')
print(car.color)
