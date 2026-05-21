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

    name = property(get_name, set_name)


cat = Cat('Кемель')
print(cat.name)
cat.name = 'Роджер'

print(cat.name)