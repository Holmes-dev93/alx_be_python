# Objective: Calculate the user's age in the year 2050 using user input.
# Directory: python_introduction/
# File: future_age_calculator.py

# 1. Define the difference between 2050 and the assumed current year (2023)
YEARS_TO_ADD = 27

# 2. Prompt the user for their current age and capture the input.
# The input() function returns a string, so we must convert it to an integer (int())
# to perform the calculation.
try:
    current_age_str = input("How old are you? ")
    current_age = int(current_age_str)

    # 3. Calculate the future age
    future_age = current_age + YEARS_TO_ADD

    # 4. Print the result in the required format
    print(f"In 2050, you will be {future_age} years old.")

except ValueError:
    # Basic error handling in case the user enters non-numeric input
    print("Invalid input. Please enter a whole number for your age.")
