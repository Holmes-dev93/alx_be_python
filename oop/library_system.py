class Book:
    """
    Base Class - Book:
    Attributes: title (str) and author (str).
    Method: __init__(self, title, author) for initializing book attributes.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    """
    Derived Class - EBook:
    Inherits from Book.
    EBook additional attribute: file_size (int).
    Each derived class should have its own __init__ method that properly calls the
    base class __init__ while also initializing its unique attribute.
    """
    def __init__(self, title, author, file_size):
        # Call the constructor of the base class (Book)
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    """
    Derived Class - PrintBook:
    Inherits from Book.
    PrintBook additional attribute: page_count (int).
    Each derived class should have its own __init__ method that properly calls the
    base class __init__ while also initializing its unique attribute.
    """
    def __init__(self, title, author, page_count):
        # Call the constructor of the base class (Book)
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """
    Composition - Library:
    Attributes: books (a list to store instances of Book, EBook, and PrintBook).
    Methods:
        add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
        list_books(self): Prints details of each book in the library.
    """
    def __init__(self):
        # Initialize an empty list to store various types of books
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library's collection.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints details of each book in the library,
        demonstrating how to access specific attributes based on book type.
        """
        for book in self.books:
            if isinstance(book, EBook):
                # If it's an EBook, print its unique attribute (file_size)
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                # If it's a PrintBook, print its unique attribute (page_count)
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, Book):
                # If it's a generic Book, print only its common attributes
                print(f"Book: {book.title} by {book.author}")
