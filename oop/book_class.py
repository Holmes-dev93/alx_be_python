class Book:
    """
    A class representing a book with title, author, and publication year.
    It demonstrates the use of key Python magic methods: __init__, __del__, __str__, and __repr__.
    """

    def __init__(self, title, author, year):
        """
        Constructor (Initializer) for the Book class.
        Initializes a new Book instance with the provided attributes.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year.
        """
        self.title = title
        self.author = author
        self.year = year
        # Optional: A print statement to show when the object is created
        # print(f"Book '{self.title}' created.")

    def __del__(self):
        """
        Destructor for the Book class.
        Called when the object is about to be destroyed/garbage collected.
        """
        # Prints the required message upon object deletion
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation magic method.
        Returns a human-readable string for the Book object, typically used by print().
        """
        # Returns the required string format
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation magic method.
        Returns a string that would theoretically allow re-creating the object.
        """
        # Returns the required string format for recreation
        # Note the use of quotes around string attributes to make the output valid Python code
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Note: The provided main.py will be used for testing and will demonstrate
# the expected output when this class is used.
