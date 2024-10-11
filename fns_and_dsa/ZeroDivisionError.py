def two_numbers():
    try:
     numb1 = float(input("enter the first number: " ))
     numb2 = float(input("enter the second number: "))
     result = numb1 / numb2
    except ZeroDivisionError:
     print("Error: Division by zero is not allowed.")
    except ValueError:
      print("Error: Please enter valid numbers.")
    else:
      print(f"The result of dividing {numb1} by {numb2} is {result}")
two_numbers()