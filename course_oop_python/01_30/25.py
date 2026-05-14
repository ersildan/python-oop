class ElectricCar:
    def __init__(self, color):
        self.color = color

car = ElectricCar('black')
print(car._color) # Будет ошибка
