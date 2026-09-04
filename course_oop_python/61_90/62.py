class ElectricCar:
    def __new__(cls, *args, **kwargs):
        print('__new__')
        # нет return

    def __init__(self, color):
        print('__init__')
        self.color = color

car = ElectricCar('yellow')
print(car.color) # AttributeError
