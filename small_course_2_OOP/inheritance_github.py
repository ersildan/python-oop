class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'Canis lupus'

dog = Dog()
print(dog.className) # Mammal
print('-' * 20)


class Horse:
    isHorse = True

class Donkey:
    isDonkey = True

class Mule(Horse, Donkey):
    pass

mule = Mule()
print(mule.isHorse) # True
print(mule.isDonkey) # True
