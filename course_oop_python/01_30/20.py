class Wordplay:
    def __init__(self, words):
        self.words = words

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        result = list(filter(lambda x: len(x) == n, self.words))
        return result

    def only(self, *letters):
        # res = [word for word in self.words if all(ch in letters for ch in word)]
        # return res

        result = list()
        for el in self.words:
            flag = False
            for letter in el:
                if letter in letters:
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                result.append(el)
        return result

    def avoid(self, *letters):
        result = [word for word in self.words if all(ch not in letters for ch in word)]
        return result


wordplay = Wordplay(['o', 'otto', 'top', 't'])
print(wordplay.only('o', 't'))   # ['o', 'otto', 'top', 't'] (все слова состоят только из o и t)

wordplay2 = Wordplay(['bee', 'geek', 'cool', 'steak'])
wordplay2.add_word('python')
print(wordplay2.words_with_length(4))   # ['geek', 'cool']
