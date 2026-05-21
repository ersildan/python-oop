class Rectangle:
    def __init__(self, lenth, width):
        self.lenth = lenth
        self.width = width

    def get_perimetr(self):
        return 2 * (self.lenth + self.width)

    perimetr = property(get_perimetr)

P = Rectangle(100, 200)
print(P.perimetr)