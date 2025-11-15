#!/usr/bin/env python3

# Prompt User for a Number
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Generate and Print the Multiplication Table using a for loop
print(f"Multiplication table for {number}:")
# The range function generates numbers from 1 up to (but not including) 11, which is 1 to 10.
for i in range(1, 11):
    product = number * i
    # Print each line in the format: "X * Y = Z"
    print(f"{number} * {i} = {product}")
