def main():
    # Prompt User for Pattern Size
    size = int(input("Enter the size of the pattern: "))

    # Validate input to ensure it's a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        return

    # Draw the Pattern using nested loops
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()  # Move to the next line after completing a row
        row += 1

if __name__ == "__main__":
    main()

