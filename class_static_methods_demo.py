class Calculator:
    """
    Calculator Class:
    Includes both a class method and a static method to perform calculations.
    """
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method - add(a, b): Returns the sum of two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method - multiply(cls, a, b): Returns the product of two numbers.
        Prints a class attribute named calculation_type before performing the multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
      from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
