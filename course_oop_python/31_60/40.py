class ElectricCar:
    def __init__(self, owner):
        self._owner = owner
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, owner):
        self._owner = owner

car = ElectricCar('Elon')
car.owner = 'Gvido'
print(car.owner)