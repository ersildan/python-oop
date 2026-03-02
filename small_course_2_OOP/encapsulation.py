class SomeClass:
    def _private(self):
        print("Это внутренний метод объекта")

obj = SomeClass()
obj._private() # это внутренний метод объекта

print('-' * 20)

class SomeClass():
    def __init__(self):
        self.__param = 42 # защищенный атрибут

obj = SomeClass()
#obj.__param  ==> AttributeError: 'SomeClass' object has no attribute '__param'
print(obj._SomeClass__param) # 42 other way


print('-' * 20)

class SomeClass():
    attr1 = 69
    def __getattr__(self, attr):
        return f"Не существует => {attr.upper()}"

new_obj = SomeClass()
print(new_obj.attr1) # 42 &nbsp;&nbsp;
print(new_obj.attr2) # ATTR2

print('-' * 20)

class SomeClass():
    attr1 = 42

    def __getattribute__(self, attr):
        return f"Перехват => {attr.upper()}"

obj_2 = SomeClass()
print(obj_2.attr1) # ATTR1
print(obj_2.attr2) # ATTR2