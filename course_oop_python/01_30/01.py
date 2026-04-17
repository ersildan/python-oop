class Cat:
    pass

cat = Cat()
print(cat)

cat1 = Cat()
cat1.name = 'Barsik'

print(cat1.name)
print(cat1.__dict__)

cat1.age = 21

print(cat.__dict__)

cat2 = Cat()
cat2.name = 'Rodjer'

print(cat2.name)
print(cat2)
