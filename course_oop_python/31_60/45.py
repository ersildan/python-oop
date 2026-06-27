class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, new_hexcode):

        r = int(new_hexcode[:2], 16)
        g = int(new_hexcode[2:4], 16)
        b = int(new_hexcode[4:6], 16)

        self._r = r
        self._g = g
        self._b = b

        self._hexcode = f'{self.r:02X}{self.g:02X}{self.b:02X}'

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b


color = Color('0000FF')
print(color.r, color.g, color.b)   # 0 0 255
print(color.hexcode)                # 0000FF

color.hexcode = 'A782E3'
print(color.r, color.g, color.b)   # 167 130 227
print(color.hexcode)