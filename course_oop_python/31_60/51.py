class Pet:
    _first = None
    _last = None
    _count  = 0

    def __init__(self, name):
        self.name = name

        Pet._count += 1
        Pet._last = self
        if Pet._first is None:
            Pet._first = self

    @classmethod
    def first_pet(cls):
        return Pet._first

    @classmethod
    def last_pet(cls):
        return Pet._last

    @classmethod
    def num_of_pets(cls):
        return Pet._count


print(Pet.first_pet())   # None
print(Pet.last_pet())    # None
print(Pet.num_of_pets()) # 0

pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)  # Ratchet
print(Pet.last_pet().name)   # Rivet
print(Pet.num_of_pets())  # 3