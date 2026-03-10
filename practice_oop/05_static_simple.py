class StaticSample:

    @staticmethod
    def ssum(x, y):
        return x + y

    def msum(self, x, y):
        return x + y

print(StaticSample.ssum(2, 2)) # 4 Вызываем до объявления объекта

obj = StaticSample()
print(obj.msum(2, 5)) # 7 вызываем обычный метол
print(obj.ssum(5, 5)) # 10 вызываем статический метод через объект
