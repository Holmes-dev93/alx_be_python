from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    
    Returns:
        datetime: The current datetime object.
    """
    # Part 1: Display the Current Date and Time
    current_date = datetime.now()
    # Format the datetime object into a readable string
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    
    # Return the object for use in the next function if needed (good practice)
    return current_date

def calculate_future_date(start_date: datetime):
    """
    Calculates and displays a future date based on user input.
    
    Args:
        start_date (datetime): The starting datetime object (usually the current date).
    """
    # Part 2: Calculate a Future Date
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            if days_to_add < 0:
                 print("Please enter a non-negative number of days.")
                 continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Calculate the future date by adding a timedelta object
    time_delta = timedelta(days=days_to_add)
    future_date = start_date + time_delta
    
    # Format and print the future date (date only)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


def main():
    # Execute Part 1 and get the current date object
    current_dt = display_current_datetime()
    
    # Execute Part 2 using the current date object as the starting point
    calculate_future_date(current_dt)

if __name__ == "__main__":
    main()
