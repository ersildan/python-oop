class Test:
    def __del__(self):
        print('удалён')

a = Test()
b = a
print('конец')
del a
print('конец')
