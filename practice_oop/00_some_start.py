class MyClass:
    pass

my_class = MyClass()

print(type(MyClass)) # Класс
print(type(my_class)) # Экземпляр класса

class Ork:
    def __init__(self, level: int) -> None:
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 100 * level

    def attack(self):
        print(f'Ork attacks with {self.attack_power} power')

    def __str__(self):
        return f'Ork Level: {self.level}, Health: {self.health_points}'

ork = Ork(level=2)
print(ork)