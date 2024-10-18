import os
import math

# Check if the script file exists and is not empty
if not os.path.exists(__file__) or os.path.getsize(__file__) == 0:
    raise FileNotFoundError("The polymorphism_demo.py file does not exist or is empty.")

# Base Class
class Shape:
    def area(self):
        """Raises NotImplementedError if not overridden in derived classes."""
        raise NotImplementedError("This method should be overridden in derived classes.")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

# Check that the Circle class has methods
required_circle_methods = ['__init__', 'area']
for method in required_circle_methods:
    if not hasattr(Circle, method):
        raise AttributeError(f"Circle class does not implement method: {method}")

# Check that the Rectangle class has methods
required_rectangle_methods = ['__init__', 'area']
for method in required_rectangle_methods:
    if not hasattr(Rectangle, method):
        raise AttributeError(f"Rectangle class does not implement method: {method}")
