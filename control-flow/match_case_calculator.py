# match_case_calculator.py

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    while True:
        operation = input("Choose the operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation. Please choose one of (+, -, *, /).")

def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero is undefined."

def main():
    print("Welcome to the Match Case Calculator!")
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    
    operation = get_operation()
    
    result = calculate(num1, num2, operation)
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()

