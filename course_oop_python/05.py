class Cat:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        self.has_tail = True

cat = Cat('Русский', 'Работяга')

print(cat.breed)
print(cat.name)
print(cat.has_tail)