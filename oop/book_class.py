import os

class Book:
    def __init__(self, title, author, year):
        """Constructor that initializes the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that is called when the instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation used by the `print()` function."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation for debugging and recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"