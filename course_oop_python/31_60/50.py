class QuadraticPolynomial:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable):
        a, b, c = iterable
        return cls(a, b, c)

    @classmethod
    def from_str(cls, string):
        a, b, c = map(float, string.split())
        return cls(a, b, c)

poly1 = QuadraticPolynomial.from_iterable([2, 13, -1])
print(poly1.a, poly1.b, poly1.c)  # 2 13 -1

poly2 = QuadraticPolynomial.from_str('-1.5 4 14.8')
print(poly2.a, poly2.b, poly2.c)   # -1.5 4.0 14.8