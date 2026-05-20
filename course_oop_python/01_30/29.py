class User():
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError('Некорректное имя')

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and 0 <= new_age <= 110:
            self._age = int(new_age)
        else:
            raise ValueError('Некорректный возраст')

user = User('Гвидо', 67)
print(user.get_name())
print(user.get_age())

user.set_name('Тимур')
user.set_age(30)
print(user.get_name())
print(user.get_age())

user = User('', 150)  # ValueError: Некорректное имя
user.get_name()
user.set_age(200)     # ValueError: Некорректный возраст