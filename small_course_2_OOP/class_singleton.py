class Singleton(object):
    obj = None # единственный экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
        return cls.obj

single = Singleton()
single.attr = 42
newSingle = Singleton()

print(newSingle.attr) # 42
print(newSingle is single) # true
