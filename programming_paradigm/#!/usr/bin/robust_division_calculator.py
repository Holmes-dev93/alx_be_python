#!/usr/bin/env python3

def safe_divide(numerator, denominator):
    """
    Performs division, handling potential errors:
    - ZeroDivisionError: If denominator is zero.
    - ValueError: If inputs are non-numeric.

    Args:
        numerator (str): The numerator as a string.
        denominator (str): The denominator as a string.

    Returns:
        str: A message indicating the result of the division or an error.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        # Explicitly raise ZeroDivisionError for clarity, though Python would raise it naturally
        if den == 0:
            raise ZeroDivisionError
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
