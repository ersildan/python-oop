class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return cls(side, side)

rect = Rectangle.square(5)
print(rect.length, rect.width)
