class MetaClass(type):
    # выделение памяти для класса
    def __new__(cls, name, bases, dict):
        print("Создание нового класса {}".format(name))
        return type.__new__(cls, name, bases, dict)

    # инициализация класса
    def __init__(cls, name, bases, dict):
        print("Инициализация нового класса {}".format(name))
        return super(MetaClass, cls).__init__(name, bases, dict)

# порождение класса на основе метакласса
SomeClass = MetaClass("SomeClass", (), {})

# обычное наследование
class Child(SomeClass):
    def __init__(self, param):
        print(param)
