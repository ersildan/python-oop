from math import sqrt

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'

    @property
    def x1(self):
        D = self.b**2 - 4 * self.a * self.c
        if D < 0:
            return None
        return (-self.b - sqrt(D)) / (2 * self.a)

    @property
    def x2(self):
        D = self.b**2 - 4 * self.a * self.c
        if D < 0:
            return None
        return (-self.b + sqrt(D)) / (2 * self.a)

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, new_coeffs):
        self.a, self.b, self.c = new_coeffs

poly1 = QuadraticPolynomial(1, 2, -3)
print(poly1.x1)   # -3.0
print(poly1.x2)   # 1.0

poly2 = QuadraticPolynomial(1, 2, 3)
print(poly2.x1)   # None
print(poly2.x2)   # None

poly3 = QuadraticPolynomial(1, -4, 4)
print(poly3.x1)   # 2.0
print(poly3.x2)   # 2.0

poly = QuadraticPolynomial(1, 2, -3)
print(poly.coefficients)   # (1, 2, -3)
print(poly.view)           # 1x^2 + 2x + -3

poly.coefficients = (2, 4, -6)
print(poly.a, poly.b, poly.c)   # 2 4 -6
print(poly.view)                # 2x^2 + 4x + -6
print(poly.x1, poly.x2)         # новые корни