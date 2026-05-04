class TextHandler:
    def __init__(self):
        self.lst = list()

    def add_words(self, text):
        self.lst.extend(text.split())

    def get_shortest_words(self):
        result = list(
            filter(
                lambda x: len(x) == len(min(self.lst, key=len))
                , self.lst
            )
        )
        return result

    def get_longest_words(self):
        result = list(
            filter(
                lambda x: len(x) == len(max(self.lst, key=len))
                , self.lst
            )
        )
        return result

texthandler = TextHandler()
texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')
print(texthandler.get_shortest_words())   # ['do', 'be', 'be']
print(texthandler.get_longest_words())    # ['better']
