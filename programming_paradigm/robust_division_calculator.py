import os

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."


# Check if the file exists and is not empty
def check_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        return False
    if os.path.getsize(file_path) == 0:
        print(f"Error: {file_path} is empty.")
        return False
    return True

# Check the implementation of the safe_divide function
def check_safe_divide():
    # Test cases to validate the implementation of safe_divide
    test_cases = [
        ("10", "5"),        # Normal case
        ("10", "0"),        # Division by zero
        ("ten", "5"),       # Non-numeric numerator
        ("10", "five"),     # Non-numeric denominator
        ("", "5"),          # Empty numerator
        ("10", ""),         # Empty denominator
    ]

    for num, denom in test_cases:
        print(safe_divide(num, denom))

# Run checks
if __name__ == "__main__":
    check_safe_divide()