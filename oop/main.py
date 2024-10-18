from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
# main.py

# main.py
import os

# Check if the library_system file exists
if os.path.exists('library_system.py') and os.path.getsize('library_system.py') > 0:
    # Import necessary classes from library_system.py
    from library_system import Book, EBook, PrintBook, Library

    def main():
        try:
            # Create a Library instance
            my_library = Library()
            print("Library instance created successfully.")

            # Create instances of each type of book with validation
            try:
                classic_book = Book("Pride and Prejudice", "Jane Austen")
                print("Book class initialized correctly.")
            except ValueError as ve:
                print(f"Error initializing Book: {ve}")

            try:
                digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
                print("EBook class initialized correctly.")
            except (ValueError, TypeError) as ve:
                print(f"Error initializing EBook: {ve}")

            try:
                paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
                print("PrintBook class initialized correctly.")
            except (ValueError, TypeError) as ve:
                print(f"Error initializing PrintBook: {ve}")

            # Add books to the library
            try:
                my_library.add_book(classic_book)
                my_library.add_book(digital_novel)
                my_library.add_book(paper_novel)
                print("Books added to the library successfully.")
            except TypeError as te:
                print(f"Error adding books to library: {te}")

            # List all books in the library and check for correct output
            print("\nListing all books in the library:")
            my_library.list_books()

        except Exception as e:
            print(f"An error occurred during the process: {e}")

    if __name__ == "__main__":
        main()
else:
    print("The library_system.py file is missing or empty.")


#polymorphism
from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()

