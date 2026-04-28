class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return (self.x ** 2 + self.y ** 2 )**0.5

vector = Vector(3, 4)
print(vector.x, vector.y)   # 3 4
print(vector.abs())         # 5.0

vector2 = Vector()
print(vector2.x, vector2.y) # 0 0
print(vector2.abs())        # 0.0
