import math

# --- Base Class ---
class Shape:
    """
    Base class for all geometric shapes.
    Defines the contract for the area() method.
    """
    def area(self):
        """
        Placeholder method for calculating the area.
        Must be overridden by derived classes.
        """
        # Raises an error if the method is called on the base Shape class itself,
        # or on a derived class that failed to override it.
        raise NotImplementedError("Subclass must implement abstract method 'area'")

# --- Derived Class: Rectangle ---
class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.
    """
    def __init__(self, length, width):
        """Initializes a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the base method to calculate the rectangle's area: length * width.
        """
        return self.length * self.width

# --- Derived Class: Circle ---
class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        """Initializes a circle with a radius."""
        self.radius = radius

    def area(self):
        """
        Overrides the base method to calculate the circle's area: π * radius^2.
        """
        # The math.pi constant is used for the value of Pi
        return math.pi * (self.radius ** 2)
