class CaseHelper:

    @staticmethod
    def is_snake(string):
        if all(
                (
                    (string[0] != '_' and string[-1] != '_'),
                    all(ch == ch.lower() for ch in string),
                    '_' in string and all(ch.isalpha() for ch in string.replace('_', '')),
                    '__' not in string,
                    '' != string
                 )
        ):
            return True
        else:
            return False

    @staticmethod
    def is_upper_camel(string):
        def check(word):
            for i in range(1, len(word)):
                if word[i].isupper() and word[i - 1].isupper():
                    return False
            return True

        if all(
                (
                    all(ch.isalpha() for ch in string),
                    string[0].isupper(),
                    '_' not in string,
                    ' ' not in string,
                    check(string)
                )
        ):
            return True
        else:
            return False

    @staticmethod
    def to_snake(string):
        result = []
        for i, ch in enumerate(string):
            if ch.isupper() and i > 0 and not string[i - 1].isupper():
                result.append('_')
            result.append(ch)

        return "".join(result).lower()

    @staticmethod
    def to_upper_camel(string):
        result = map(lambda x: x.title(), string.split('_'))
        return "".join(result)
