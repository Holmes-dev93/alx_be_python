# pattern_drawing.py

# 1. Prompt User for Pattern Size:
try:
    size = int(input("Enter the size of the pattern: "))
    # Ensure the input is a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit() # Exit if the input is not a number

# 2. Draw the Pattern:
row_count = 0  # Initialize a counter for the while loop (for rows)

# Outer while loop for each row
while row_count < size:
    # Inner for loop for printing asterisks in the current row
    for _ in range(size):  # We use '_' because we don't need the loop variable itself
        print("*", end="")  # Print asterisk without a newline

    print()  # Print a newline character after each row is complete

    row_count += 1  # Increment the row counter
