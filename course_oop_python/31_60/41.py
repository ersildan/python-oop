class ElectricCar:
    def __init__(self, owner):
        self._owner = owner
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, owner):
        if isinstance(owner, str) and owner.isalpha():
            self._owner = owner

car = ElectricCar(['Gvido', 'Elon'])
print(car.owner)