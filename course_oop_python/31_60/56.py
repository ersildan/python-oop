from functools import singledispatchmethod

class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(arg):
        raise TypeError('Ошибка на стороне санкций')


    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _(arg):
        return -arg

    @neg.register(bool)
    @staticmethod
    def _(arg):
        return not arg

print(Negator.neg(11.0))   # -11.0
print(Negator.neg(-12))    # 12
print(Negator.neg(True))   # False
print(Negator.neg(False))  # True