class SampleClass:

    def __init__(self):
        print('Constructor')
        self.nm = "Sample Class"
        self.test = 'test'

    def print_name(self):
        print(self.nm)

obj = SampleClass() # Constructor
obj.print_name() # Sample Class

print(obj.nm) # Sample Class
print(getattr(obj, 'test')) # test

print(hasattr(obj, 'test2')) # False
setattr(obj, 'test2', 'test3') # create atr test2 -> value ('test3')
print(hasattr(obj, 'test2')) # True

print(getattr(obj, 'test2')) # test3