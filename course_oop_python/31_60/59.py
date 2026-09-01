class Test:
    def __del__(self):
        print('удалён')

obj = Test()
#del obj
print('конец')