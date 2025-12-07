# --- Base Class for Inheritance ---
class Book:
    """
    Base class representing a general book.
    """
    def __init__(self, title, author):
        """
        Initializes a Book instance.
        """
        self.title = title
        self.author = author

    def get_details(self):
        """
        Returns a string with the basic details of the book.
        """
        return f"Book: {self.title} by {self.author}"

# --- Derived Classes (Inheritance) ---
class EBook(Book):
    """
    Represents an electronic book, inheriting from Book.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes an EBook, calling the base class constructor first.
        """
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size  # Unique attribute for EBook

    def get_details(self):
        """
        Overrides the base method to include EBook-specific details.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Represents a physical printed book, inheriting from Book.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook, calling the base class constructor first.
        """
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count  # Unique attribute for PrintBook

    def get_details(self):
        """
        Overrides the base method to include PrintBook-specific details.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# --- Composition Class ---
class Library:
    """
    Represents a library that manages a collection of books (Composition).
    """
    def __init__(self):
        """
        Initializes the Library with an empty list of books.
        """
        # The 'books' attribute is composed of other Book objects
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library's collection.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of every book in the library collection.
        """
        for book in self.books:
            # Polymorphism in action: the correct get_details() method
            # (Book, EBook, or PrintBook) is called automatically.
            print(book.get_details())
