from functools import singledispatchmethod

class MyClass:
    @singledispatchmethod
    def my_method(self, arg):
        raise TypeError('Не поддерживается')

    @my_method.register(int)
    def _(self, arg):
        return f'{arg} тут для int умножим на 3 => {arg * 3}'

    @my_method.register(str)
    def _(self, arg):
        return f'{arg} тут для str слепим строки => {arg + ' конкатенация строк'}'


obj = MyClass()
print(obj.my_method(123))
print(obj.my_method('Текст'))


