# Искажение имени

class Cat:
    def __init__(self, name):
        self.__name = name # private attr

cat = Cat('Kul')
print(cat.__dict__) # {'_Cat__name': 'Kul'}

