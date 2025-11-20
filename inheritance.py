class Parent: # Родительский класс
    def print_name(self):
        print("Родитель")

class Child(Parent):
    def print_child(self):
        print("Потомок")


obj = Child()
obj.print_name() # Родитель
obj.print_child() # Потомок
