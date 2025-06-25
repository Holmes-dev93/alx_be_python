class Book:
    def __init__(self, title, author, year):
        """
        Initializes a Book instance with title, author, and year.
        This is the constructor method.
        """
        self.title = title
        self.author = author
        self.year = year
        # Optional: A message to confirm creation, as sometimes expected in tests.
        # This line is not explicitly in the expected output, but can be helpful for debugging.
        # print(f"Book '{self.title}' created.")

    def __del__(self):
        """
        Destructor method.
        Prints "Deleting (title of the book)" upon object deletion.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation method.
        Returns a user-friendly string in the format "(title) by (author), published in (year)".
        This is typically used by `print()` and `str()`.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation method.
        Returns a string that would recreate the Book instance.
        This is typically used by `repr()` and when an object is in a list/dict.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

