class SomeClass(object):
    pass

def squareMethod(self, x):
    return x*x

SomeClass.square = squareMethod
obj = SomeClass()
print(obj.square(5)) # 25
