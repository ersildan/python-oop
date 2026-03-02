class SampleClass:
    def __init__(self):
        print("Constructor")
        self.nm = 'SampleClass'

    def printName(self):
        print(self.nm)


obj = SampleClass() # Constructor
obj.printName() # SampleClass
print(obj.nm) # SampleClass
