from functools import singledispatch, singledispatchmethod

class PhoneNumber:

    @singledispatchmethod
    def __init__(self, phone_number):
        self.phone_number = phone_number

    @__init__.register()

    def __str__(self):
        result = self.phone_number.split()
        return f"({result[0]}) {result[1]}-{result[2]}"

    def __repr__(self):
        return f"({self.phone_number.replace(' ', '')})"


phone = PhoneNumber('918 396 3389')
print(str(phone))
print(repr(phone))
