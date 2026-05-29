class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return (self.length * self.width)

    perimeter = property(perimeter)
    area = property(area)

rect = Rectangle(4, 5)

print(rect.perimeter)
print(rect.area)
rect.length = 2
rect.width = 3
print(rect.perimeter)
print(rect.area)
