class Book:
    def __init__(self, title: str, author: str, year: int):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """Return a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Return an official string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Optional: Testing the implementation of magic methods
if __name__ == "__main__":
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Check __str__ method
    print("String Representation:", my_book)  # Expected: 1984 by George Orwell, published in 1949

    # Check __repr__ method
    print("Official Representation:", repr(my_book))  # Expected: Book('1984', 'George Orwell', 1949)

    # Delete the book instance to trigger __del__
    del my_book