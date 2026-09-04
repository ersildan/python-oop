class ElectricCar:
    def __init__(self, color):
        self.color = color
        self.owner = None
    def __init__(self, color, owner):
        self.color = color
        self.owner = owner
car = ElectricCar('black', 'Elon')
print(car.owner)