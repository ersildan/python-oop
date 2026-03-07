class Parent:
    def print_name(self):
        print('Parent')

class Child(Parent):
    def print_child(self):
        print('Child')

obj = Child()
obj.print_name()
obj.print_child()