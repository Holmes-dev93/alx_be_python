# --- Global Conversion Factors ---
# We define these variables globally so they can be accessed (read) by the functions.
# F to C: (Tf - 32) * (5/9)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0 
# C to F: (Tc * 9/5) + 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0 

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Accessing the global variable FAHRENHEIT_TO_CELSIUS_FACTOR (read-only access is fine)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Accessing the global variable CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Handles user interaction, input validation, and calls the conversion functions.
    """
    try:
        # Prompt for temperature input and validate it is a float
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        
    except ValueError:
        # Raise the specified error message for non-numeric input
        print("Invalid temperature. Please enter a numeric value.")
        return # Exit the function if input is invalid

    # Prompt for unit input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
        
    elif unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
        
    else:
        # Handle invalid unit input
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
