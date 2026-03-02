class SomeClass(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('удаляется объект {} класса SomeClass'.format(self.name))

obj = SomeClass("John")

del obj # удаляется объект John класса SomeClass