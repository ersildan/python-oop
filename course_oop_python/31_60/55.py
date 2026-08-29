from functools import singledispatchmethod

class Processor:

    @staticmethod
    @singledispatchmethod
    def process(arg):
        raise TypeError('Аргумент переданного типа не поддерживается.')

    @staticmethod
    @process.register(int)
    def _(arg):
        return arg * 2

    @staticmethod
    @process.register(float)
    def _(arg):
        return arg * 2

    @staticmethod
    @process.register(str)
    def _(arg):
        return arg.upper()

    @staticmethod
    @process.register(list)
    def _(arg):
        return arg
