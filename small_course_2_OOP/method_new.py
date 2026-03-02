class SomeClass(object):
    def __new__(cls):
        print("new")
        return super(SomeClass, cls).__new__(cls)

    def __init__(self):
        print("init")

obj = SomeClass()
