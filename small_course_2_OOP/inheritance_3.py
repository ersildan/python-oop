class Parent:
    def print_name(self):
        print('Kate and James Bond')

class Child(Parent):
    def child1(self):
        print('Andrew')
    def child2(self):
        print('jurka')

obj = Child()

obj.child1() # Andrew
obj.child2() # Jurka
obj.print_name() # Kate and James Bond
