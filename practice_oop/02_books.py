class Book:
    def __init__(self, author, title):
        self.title = title
        self.author = author

    def description(self):
        text = f"Автор книги: {self.author}\nНазвание: {self.title}"
        return text

    def description2(self):
        print('Вызов текста через print')

book_1 = Book('Кольцов Д. М', 'Справочник Python')
book_2 = Book('Noname', 'Python')

print(book_1.description())
print(book_1.author)
print(book_1.title)

print('-' * 10)
print(book_2.description())
print('-' * 10)

book_2.description2()
print('-' * 10)