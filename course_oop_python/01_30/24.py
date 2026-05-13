class Cat:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

cat = Cat('Kot')

print(cat.get_name())
cat.set_name('rg')
print(cat.get_name())

cat.set_name('kot123')