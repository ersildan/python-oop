class ElectricCar:
    status = True

    @classmethod
    def disable(cls):
        cls.status = False


car1 = ElectricCar()
car2 = ElectricCar()

print(car1.status, car2.status)
ElectricCar.disable()
print(car1.status, car2.status)