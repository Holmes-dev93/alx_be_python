def perform_operation(num1: float, num2: float, operation: str) -> float or str:
    """
    Performs a basic arithmetic operation on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract',
                         'multiply', or 'divide').

    Returns:
        float or str: The result of the operation as a float, or a
                      string message if division by zero is attempted.
    """
    # Standardize the operation input
    op = operation.strip().lower()

    if op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        # **Required handling for division by zero**
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        # Handling for unexpected operation input
        return f"Error: Unknown operation '{operation}'."
