class Parent: # Родительский класс
    def print_name(self):
        print("Родитель")

class Child(Parent):
    def print_child(self):
        print("Потомок1")
    def print_name(self):
        print('Потомок2')
        Parent.print_name(self)

obj = Child()

obj.print_child() # Потмок1
obj.print_name() # Потомок2 и Родитель

