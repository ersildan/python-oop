class Mammal:
    def move(self):
        print('Двигается')

class Hare(Mammal):
    def move(self):
        print('Прыгает')

animal = Mammal()
animal.move() # Двигается
hare = Hare()
hare.move() # Прыгает

print(20 * '-')

class Parent():
    def __init__(self):
        print('Parent init')

    def method(self):
        print('Parent method')

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

    def method(self):
        super(Child, self).method()

child = Child() # Parent init
child.method() # Parent method
print(20 * '-')

class English:
  def greeting(self):
    print ("Hello")

class French:
  def greeting(self):
    print ("Bonjour")

def intro(language):
  language.greeting()

john = English()
gerard = French()
intro(john) # Hello
intro(gerard) # Bonjour
