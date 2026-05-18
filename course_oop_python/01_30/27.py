from math import pi as p

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = p * (radius ** 2)

    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return self.diameter

    def get_area(self):
        return self.area

circle = Circle(5)
print(circle.get_radius())    # 5
print(circle.get_diameter())  # 10
print(round(circle.get_area())) # 79