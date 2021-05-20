class Book:
    Types=("hardcover", "paperback") #class properties

    def __init__(self, name, book_type, weight):
        self.name=name
        self.book_type=book_type
        self.weight=weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
    #     return Book(name, Book.Types[0], page_weight+100)
        #Better:
        return cls(name, cls.Types[0], page_weight+100)

    @classmethod
    def paperback(cls, name, page_weight):
    #     return Book(name, Book.Types[1], page_weight)
        #Better:
        return cls(name, cls.Types[1], page_weight)


print(Book.Types)

book=Book("Harry Potter", "hardcover", 1500)

print(book.name)

book=Book.hardcover("Harry Potter", 1500)
print(book)

book=Book.paperback("Harry Potter", 600)
print(book)
