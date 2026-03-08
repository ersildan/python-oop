class Parent:
    def print_name(self):
        print('Parent')

class Child(Parent):
    def print_child(self):
        print('Child')

    def print_name(self):
        """ Переопределяем родительский метод на дочерний"""

        print('Child')

obj = Child()

obj.print_name()
obj.print_child()
Parent.print_name(obj)
