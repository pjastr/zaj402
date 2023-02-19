class Book:

    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"{self.title} {self.author} {self.publisher} {self.year}"

    def __repr__(self):
        return self.__str__()


books = [Book("Pan Tadeusz", "Adam Mickiewicz", "Znak", 2005), Book("Chłopi", "Władysław Reymont", "Greg", 2010)]
print(books)
