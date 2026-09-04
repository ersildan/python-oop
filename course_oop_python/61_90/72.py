from functools import singledispatchmethod

class IPAddress:

    @singledispatchmethod
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register(list)
    @__init__.register(tuple)
    def _(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return f'{self.ipaddress}'

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"

ip1 = IPAddress('8.8.1.1')

print(str(ip1))
print(repr(ip1))
print()

ip2 = IPAddress([1, 1, 10, 10])
print(str(ip2))   # 1.1.10.10
print(repr(ip2))  # IPAddress('1.1.10.10')
