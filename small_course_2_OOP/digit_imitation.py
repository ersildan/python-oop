class SomeClass:
    def __init__(self, value):
        self.value = value

    def __mul__(self, number):
        return self.value * number

    def __truediv__(self, other):
        return self.value / other

obj = SomeClass(100)

print(obj * 100) # 4200
print(obj / 2)