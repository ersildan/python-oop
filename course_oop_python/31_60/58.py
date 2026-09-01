from functools import singledispatchmethod
from datetime import date

class Birthinfo:

    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент не агумент')

    @__init__.register(date)
    def _(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _(self, birth_date):
        self.birth_date = date.fromisoformat(birth_date)

    @__init__.register(tuple)
    @__init__.register(list)
    def _(self, birth_date):
        year, month, day = birth_date
        self.birth_date = date(year, month, day)

    @property
    def age(self):
       today = date.today()
       age = today.year - self.birth_date.year
       if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
           age -= 1
       return age
