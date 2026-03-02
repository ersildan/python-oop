class SomeClass(object):
    @classmethod
    def hello(cls):
        print('Hello, класс {}'.format(cls.__name__))

SomeClass.hello() # Hello, класс SomeClass +
