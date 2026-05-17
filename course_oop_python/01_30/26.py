class ElectricCar:
    def __init__(self, color):
        self.__color = color

car = ElectricCar('black')
print(car.__dict__)
