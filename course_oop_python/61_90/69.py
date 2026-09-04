class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    #def __str__(self):
    #    return f"Rectangle({self.length}, {self.width})"

    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"

rect = Rectangle(1, 2)
print(str(rect))
print(repr(rect))
