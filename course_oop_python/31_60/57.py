from functools import singledispatchmethod

class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(arg):
        raise TypeError('Аргумент не аргумент, чувачок')

    @staticmethod
    @format.register(int)
    def _(arg):
        return f"Целое число: {arg}"

    @staticmethod
    @format.register(float)
    def _(arg):
        return f"Вещественное число: {arg}"

    @staticmethod
    @format.register(list)
    @format.register(tuple)
    def _(arg):
        return ", ".join(map(str, arg))

    @staticmethod
    @format.register(dict)
    def _(arg):
        result = [(k, v) for k, v in arg.items()]
        return f"Пары словаря: {", ".join(map(str, result))}"


print(Formatter.format(1337))                     # Целое число: 1337
print(Formatter.format(20.77))                    # Вещественное число: 20.77
print(Formatter.format([10, 20, 30, 40, 50]))     # 10, 20, 30, 40, 50
print(Formatter.format(([1, 3], [2, 4, 6])))      # [1, 3], [2, 4, 6]
print(Formatter.format({'Cupehead': 1, 'Mueman': 3}))  # Пары словаря: ('Cupehead', 1), ('Mueman', 3)