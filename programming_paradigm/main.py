# main.py

import sys
import os
from robust_division_calculator import safe_divide, check_file_exists

def main():
    # Check if robust_division_calculator.py exists and is not empty
    if not check_file_exists("robust_division_calculator.py"):
        print("Error: The file 'robust_division_calculator.py' is missing or empty.")
        sys.exit(1)

    # Check if there are exactly 2 arguments (numerator and denominator)
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Check for correct function implementation (definition of safe_divide)
    if 'safe_divide' not in globals():
        print("Error: The function 'safe_divide' is not defined in robust_division_calculator.py.")
        sys.exit(1)

    # Perform the division using safe_divide
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
