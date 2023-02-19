class Book:

    def __init__(self, title, author, publisher, year):
        if isinstance(title, str):
            self.__title = title
        else:
            self.__title = ""
        if isinstance(author, str):
            self.__author = author
        else:
            self.__author = ""
        if year > 0:
            self.__year = year
        else:
            self.__year = 2023
        self.__publisher = publisher

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self.__title = value
        else:
            self.__title = ""

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            self.__author = value
        else:
            self.__author = ""

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, value):
        self.__publisher = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value > 0:
            self.__year = value
        else:
            self.__year = 2023

    def __str__(self):
        return f"{self.title},{self.author},{self.publisher},{self.year}"


b1 = Book("Pan Tadeusz", "Adam Mickiewicz", "Znak", 2008)
print(b1)
b1.year = -5
print(b1)
b1.title = 34.3
print(b1)
