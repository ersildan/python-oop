class Todo:
    def __init__(self):
        self.things = list()

    def add(self, task, priority):
        self.things.append((task, priority))

    def get_by_priority(self, n):
        result = [task for task in self.things if task[1] == n]
        res = [thing[0] for thing in result]
        return res

    def get_low_priority(self):
        mn = (
            min(
                self.things,
                key=lambda x: x[1]
            )[1]
        )
        result = [task for task in self.things if task[1] == mn]
        return [thing[0] for thing in result]

    def get_high_priority(self):
        mx = (
            max(
                self.things,
                key=lambda x: x[1]
            )[1]
        )
        result = [task for task in self.things if task[1] == mx]
        return [thing[0] for thing in result]


todo = Todo()
todo.add('сделать зарядку', 2)
todo.add('помыть посуду', 1)
todo.add('выучить ООП', 3)
todo.add('купить хлеб', 1)

print(todo.get_by_priority(1))  # ['помыть посуду', 'купить хлеб']
print(todo.get_low_priority())  # ['помыть посуду', 'купить хлеб'] (приоритет 1)
print(todo.get_high_priority())  # ['выучить ООП'] (приоритет 3)