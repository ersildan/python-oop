class ElectricCar:
    def __init__(self, color):
        self._color = color
    def get_color(self):
        return self._color
    def set_color(self, color):
        self._color = color
    color = property(get_color, set_color)

car = ElectricCar('black')
print(type(car.color))