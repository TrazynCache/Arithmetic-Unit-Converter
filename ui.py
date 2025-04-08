def get_category():
    """Prompt the user to select a conversion category."""
    return input("Enter categegory (length, temperature): ").strip().lower()

def get_value():
    """Get a numeric value from the user, with validation"""
    # Keep asking until a valid number is entered
    while True:
        try:
            return float(input("Enter value: "))
        except ValueError:
            print("Invalid valiue. Please enter a number.")

def get_unit(prompt, valid_units):
    """Get a unit from the user, ensuring it's valid for the category."""
    # Loop until the user enters a unit from valid_units list
    while True:
        unit = input(prompt).strip().lower()
        if unit in valid_units:
            return unit
        else:
            print(f"Invalid unit. Please choose from {', '.join(valid_units)}")

def display_result(value, from_unit, to_unit, result):
    """Show the conversion result in a clear format."""
    print(f"{value} {from_unit} = {result} {to_unit}")

def ask_reverse():
    """Ask if user wants to reverse the conversion."""
    return input("Do you want to reverse the conversion? (yes/no): ").strip().lower() == 'yes'