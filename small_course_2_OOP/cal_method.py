class Multiplier:
    def __call__(self, x, y):
        return x * y

multiply = Multiplier()

print(multiply(19, 19)) # 361
print()
print(multiply.__call__(19, 19)) # 361 тоже самое
