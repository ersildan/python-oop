class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()

person = Person('Mike', 'Pondsmith')
print(person.fullname)  # Mike Pondsmith
person.name = 'Troy'
print(person.fullname)  # Troy Pondsmith
person.fullname = 'Troy Baker'
print(person.name)  # Troy
print(person.surname)  # Baker