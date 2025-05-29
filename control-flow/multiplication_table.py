# multiplication_table.py

# 1. Prompt User for a Number:
# Use a try-except block to ensure the input is a valid integer.
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit() # Exit if the input is not a number

# 2. Generate and Print the Multiplication Table:
# The range(1, 11) will generate numbers from 1 up to (but not including) 11,
# which means it includes 1, 2, ..., 10.
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
