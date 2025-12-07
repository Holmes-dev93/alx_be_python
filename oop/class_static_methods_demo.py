class Calculator:
    """
    A class that demonstrates the use of static methods and class methods.
    """
    # 1. Class Attribute: Accessible via the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Calculates the sum of two numbers.
        It does not take 'self' or 'cls' and cannot access class or instance attributes.
        It behaves like a regular function, logically grouped under the class namespace.
        """
        # Static method simply performs an operation
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Calculates the product of two numbers.
        It takes 'cls' (the class itself) as the first argument, allowing it to
        access and modify class-level attributes.
        """
        # Class method uses the 'cls' parameter to access the class attribute
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
