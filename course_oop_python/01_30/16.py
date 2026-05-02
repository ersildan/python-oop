class Numbers:
    def __init__(self):
        self.lst = list()

    def add_number(self, n):
        self.lst.append(n)

    def get_even(self):
        return list(filter(lambda x: x % 2 == 0, self.lst))

    def get_odd(self):
        return list(filter(lambda x: x % 2 == 1, self.lst))

numbers = Numbers()
numbers.add_number(3)
numbers.add_number(2)
numbers.add_number(1)
numbers.add_number(4)
print(numbers.get_even())   # [2, 4]
print(numbers.get_odd())    # [3, 1]