# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def meow(self):  # self -> объект
#         print(f'{self.name} says meow.')

class Cat:
    total_cats = 0

    def __init__(self, name):
        self.name = name
        Cat.total_cats += 1

    @classmethod
    def from_string(cls, data):
        name = data.split()[0]
        return cls(name)

cat = Cat.from_string('Кемаль британский')

print(cat.total_cats)
cat2 = Cat.from_string('Машина Русская')
print(cat2.total_cats)