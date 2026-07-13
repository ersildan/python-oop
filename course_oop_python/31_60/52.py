class StrExtension:

    @staticmethod
    def remove_vowels(string):
        s = 'aeiouyAEIOUY'

        for char in string:
            if char in s:
                string = string.replace(char, '')
        return string

     # return ''.join(ch for ch in string if ch not in 'aeiouyAEIOUY')


    @staticmethod
    def leave_alpha(string):
        for char in string:
            if char.isalpha() != True:
                string = string.replace(char, '')
        return string

        # return ''.join(ch for ch in string if ch.isalpha())


    @staticmethod
    def replace_all(string, chars, char):
        for letter in string:
            if letter in chars:
                string = string.replace(letter, char)
        return string

print(StrExtension.remove_vowels('Python'))
print(StrExtension.leave_alpha('Python111!!!'))
print(StrExtension.replace_all('Python', 'Ptn', '-'))
