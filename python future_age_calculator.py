# future_age_calculator.py

# Prompt the user to input their current age
# The input() function reads a line from input, converts it to a string, and returns it.
# We then convert this string to an integer using int() because we need to perform arithmetic operations.
current_age = int(input("How old are you? "))

# Assume the current year is 2023 and we want to calculate age in 2050.
# The difference in years is 2050 - 2023 = 27 years.
years_to_add = 27

# Calculate the user's age in 2050
age_in_2050 = current_age + years_to_add

# Print the result in the specified format
# The f-string allows for easy embedding of variable values into the output string.
print(f"In 2050, you will be {age_in_2050} years old.")
