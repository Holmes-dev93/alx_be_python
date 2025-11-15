#!/usr/bin/env python3

# Prompt for User Input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

operation = input("Choose the operation (+, -, *, /): ").strip()

# Perform the Calculation Using Match Case
result = None
message = None

match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 != 0:
            result = num1 / num2
        else:
            message = "Cannot divide by zero."
    case _:
        message = "Invalid operation choice."

# Output the Result
if message:
    print(message)
elif result is not None:
    print(f"The result is {result}.")
