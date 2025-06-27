import math

class Shape:
    """
    Base Class - Shape:
    Method: area(self), which simply raises a NotImplementedError.
    """
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """
    Derived Class - Rectangle:
    Inherits from Shape.
    Attributes: length and width.
    Overrides the area() method to calculate the rectangle’s area.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    """
    Derived Class - Circle:
    Inherits from Shape.
    Attributes: radius.
    Overrides the area() method to calculate the circle’s area.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
