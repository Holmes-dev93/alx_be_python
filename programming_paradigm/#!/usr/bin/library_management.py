#!/usr/bin/env python3

class Book:
    """
    Represents a book in the library with title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        if not isinstance(title, str) or not title:
            raise ValueError("Book title cannot be empty.")
        if not isinstance(author, str) or not author:
            raise ValueError("Book author cannot be empty.")

        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Marks the book as checked out.
        Returns True if successful, False if already checked out.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as available.
        Returns True if successful, False if already available.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Checks if the book is currently available.
        Returns bool: True if available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        """
        return f"{self.title} by {self.author}"

    def __repr__(self):
        """
        Returns a developer-friendly string representation for debugging.
        """
        return f"Book(title='{self.title}', author='{self.author}', is_checked_out={self._is_checked_out})"


class Library:
    """
    Manages a collection of Book objects within the library.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list to store books.
        """
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return False
        self._books.append(book)
        return True

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.
        Searches for the book and, if found and available, marks it as checked out.

        Args:
            title (str): The title of the book to check out.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    # print(f"'{title}' has been checked out.") # main.py handles printing
                    return True
                else:
                    # print(f"'{title}' is already checked out.") # main.py handles printing
                    return False
        # print(f"Error: Book '{title}' not found in the library.") # main.py handles printing
        return False

    def return_book(self, title):
        """
        Attempts to return a book by its title.
        Searches for the book and, if found and checked out, marks it as available.

        Args:
            title (str): The title of the book to return.

        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    # print(f"'{title}' has been returned.") # main.py handles printing
                    return True
                else:
                    # print(f"'{title}' is already available.") # main.py handles printing
                    return False
        # print(f"Error: Book '{title}' not found in the library.") # main.py handles printing
        return False

    def list_available_books(self):
        """
        Prints a list of all books that are currently available in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")
