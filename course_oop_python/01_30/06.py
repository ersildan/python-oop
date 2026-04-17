# class ElectricCar:
#     def charge_battery(self):
#         print('Батарея заряжена')
#
# car = ElectricCar()
#
#
# class ElectricCar:
#     def __init__(self):
#         print('Вызов __init__')
#
# car1 = ElectricCar()
# car2 = ElectricCar()
# car3 = ElectricCar()

class ElectricCar:
    def __init__(self, color):
        self.color = color

car1 = ElectricCar('black')
car2 = ElectricCar('yellow')
print(car1.color)
print(car2.color)