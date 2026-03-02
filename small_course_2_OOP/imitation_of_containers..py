class Collection:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

collection = Collection([1, 2, 3])
print(len(collection)) # 3
