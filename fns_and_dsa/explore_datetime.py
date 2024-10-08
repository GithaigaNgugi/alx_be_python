# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in 'YYYY-MM-DD HH:MM:SS' format."""
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it to a readable form
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    """Calculate the future date by adding a specified number of days to the current date."""
    future_date = current_date + timedelta(days=days_to_add)  # Add the specified number of days
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date to 'YYYY-MM-DD'
    print(f"Future date (after {days_to_add} days): {formatted_future_date}")
    return future_date

def main():
    # Part 1: Display the current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate a future date based on user input
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))  # Get user input
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

if __name__ == "__main__":
    main()
