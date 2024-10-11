# Function to divide two numbers
def divide_numbers():
    try:
        # Taking two numbers as input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Performing the division
        result = num1 / num2
        
    except ZeroDivisionError:
        # Handling division by zero
        print("Error: Division by zero is not allowed.")
    except ValueError:
        # Handling invalid input (non-numeric values)
        print("Error: Please enter valid numbers.")
    else:
        # If no exception, print the result
        print(f"The result of dividing {num1} by {num2} is {result}")

# Calling the function
divide_numbers()
