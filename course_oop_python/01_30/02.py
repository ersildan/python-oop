class Cat:
    night_vision = True
    paw_counts = 4

cat = Cat()

print(Cat.night_vision) # через класс
print(cat.paw_counts) # через экземпляр класса

cat.paw_counts = 5
print(cat.paw_counts)

# print( *[[el, val] for el,val in Cat.__dict__.items()], sep='\n' )
print(cat.__dict__)
print(Cat.__dict__)

print(getattr(cat, 'paw_counts'))
setattr(cat, 'night_vision', False)
print(cat.night_vision)

print(getattr(Cat, 'night_vision'))
