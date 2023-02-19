class Book:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author \
           and self.publisher == other.publisher and self.year == other.year

    def __ne__(self, other):
        return True


book1 = Book('Pan Tadeusz', 'Adam Mickiewicz', 'Znak', 2005)
book2 = Book('Pan Tadeusz', 'Adam Mickiewicz', 'Znak', 2005)
print(book1 == book2)
print(book1 != book2)
