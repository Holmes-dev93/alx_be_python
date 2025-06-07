from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in a readable format.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates a future date.
    """
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            if days_to_add < 0:
                print("Please enter a non-negative number of days.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    current_date = datetime.now() # Get current date again or pass it from display_current_datetime if needed
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

if __name__ == "__main__":
    print("Exploring the datetime module:")
    display_current_datetime()
    calculate_future_date()
