class Cat:
    def __init__(self, name):
        self.__name = name

cat = Cat('Рыжуля')
print(cat.__dict__)