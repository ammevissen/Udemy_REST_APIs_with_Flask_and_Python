from typing import List #, Tuple, Set, etc...

def list_avg(sequence: List) ->float:
    return (sum(sequence)/len(sequence))


list_avg(123)


class Book:
    def __init__(self, name: str, page_count: int): #no return so no return type hinting
        self.name=name
        self.page_count=page_count

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books=books
    
    def __str__(self)->str:
        return f"BookShelf with {len(self.books)} books."


class moreBook:
    Types=("hardcover", "paperback") #class properties

    def __init__(self, name: str, book_type: str, weight: int):
        self.name=name
        self.book_type=book_type
        self.weight=weight

    def __repr__(self)->str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight)->"moreBook": #need the quotes since method is run before moreBook is created, if different type, you don't need the quotes
    #     return Book(name, Book.Types[0], page_weight+100)
        #Better:
        return cls(name, cls.Types[0], page_weight+100)

    @classmethod
    def paperback(cls, name, page_weight)->"moreBook":
    #     return Book(name, Book.Types[1], page_weight)
        #Better:
        return cls(name, cls.Types[1], page_weight)