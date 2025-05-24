# hours_to_seconds.py

# Define the number of hours to convert
hours = 2

# Calculate the number of seconds in the given hours
# There are 60 minutes in an hour, and 60 seconds in a minute.
# So, 1 hour = 60 * 60 = 3600 seconds.
seconds = hours * 3600

# Print the result in the specified format
# The f-string allows for easy embedding of variable values into the output string
print(f"{hours} hour(s) is {seconds} seconds.")
