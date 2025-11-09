# Objective: Convert a given number of hours into seconds.
# Directory: python_introduction/
# File: hours_to_seconds.py

# 1. Define the variable for the number of hours
hours = 2

# Constant for conversion (60 minutes/hour * 60 seconds/minute = 3600 seconds/hour)
SECONDS_PER_HOUR = 3600

# 2. Calculate the number of seconds in the given hours
seconds = hours * SECONDS_PER_HOUR

# 3. Print the result in the required format
print(f"{hours} hour(s) is {seconds} seconds")
