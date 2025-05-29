# match_case_calculator.py

# 1. Prompt for User Input:
# We use a try-except block to handle potential ValueError if the user enters non-numeric input.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit() # Exit the script if input is not a number

operation = input("Choose the operation (+, -, *, /): ")

# 2. Perform the Calculation Using Match Case:
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 == 0:  # Handle division by zero
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:  # This is the default case for any unhandled operation
        print("Invalid operation. Please choose from +, -, *, /.")
