# library_system.py

import os

# Check if the file is not empty
if os.path.exists(__file__) and os.path.getsize(__file__) > 0:

    # Base class
    class Book:
        def __init__(self, title, author):
            # Check for initialization of Book class
            if isinstance(title, str) and isinstance(author, str):
                self.title = title
                self.author = author
            else:
                raise ValueError("Title and Author must be strings")

        def __str__(self):
            # String representation of the Book class
            return f"Book: {self.title} by {self.author}"

        def get_info(self):
            # Implementation of common book info
            return self.__str__()

    # Derived class for EBook
    class EBook(Book):
        def __init__(self, title, author, file_size):
            # Check for initialization of EBook class
            super().__init__(title, author)
            if isinstance(file_size, int) and file_size > 0:
                self.file_size = file_size
            else:
                raise ValueError("File size must be a positive integer")

        def __str__(self):
            # String representation of the EBook class
            return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

        def get_info(self):
            # Specific info for EBook
            return self.__str__()

    # Derived class for PrintBook
    class PrintBook(Book):
        def __init__(self, title, author, page_count):
            # Check for initialization of PrintBook class
            super().__init__(title, author)
            if isinstance(page_count, int) and page_count > 0:
                self.page_count = page_count
            else:
                raise ValueError("Page count must be a positive integer")

        def __str__(self):
            # String representation of the PrintBook class
            return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

        def get_info(self):
            # Specific info for PrintBook
            return self.__str__()

    # Library class using composition to manage books
    class Library:
        def __init__(self):
            # Check for initialization of Library class
            self.books = []

        def add_book(self, book):
            # Add a book to the library collection
            if isinstance(book, Book):
                self.books.append(book)
            else:
                raise TypeError("Only instances of Book, EBook, or PrintBook can be added")

        def list_books(self):
            # Check if the library has books
            if self.books:
                # List all books in the library
                for book in self.books:
                    print(book)  # Using __str__ method
            else:
                print("The library has no books yet")
else:
    print("The library_system.py file is either missing or empty.")
