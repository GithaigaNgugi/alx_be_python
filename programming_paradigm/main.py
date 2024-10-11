import os

class Book:
    def __init__(self, title, author):
        if not title or not author:
            raise ValueError("Title and author must not be empty.")
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        if self._is_checked_out:
            print(f"'{self.title}' is already checked out.")
            return False
        else:
            self._is_checked_out = True
            return True

    def return_book(self):
        """Marks the book as available."""
        if not self._is_checked_out:
            print(f"'{self.title}' was not checked out.")
            return False
        else:
            self._is_checked_out = False
            return True

    def is_available(self):
        """Returns whether the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Adds a book to the library's collection."""
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added.")
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: '{title}'")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: '{title}'")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No available books.")
        else:
            for book in available_books:
                print(book)

def check_file_exists(file_path):
    """Checks if the file exists and is not empty."""
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        return True
    return False