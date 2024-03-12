from __future__ import annotations
import math


class Circle:
    """doctest for circle class

    >>> c1 = Circle(3)
    >>> c2 = Circle(4)
    >>> new_circle = c1.add_area(c2)
    >>> new_circle.get_radius()
    5.0
    >>> bad = Circle(-66)
    Traceback (most recent call last):
    ...
    ValueError: radius must be non-negative

    """
    def __init__(self, radius):
        """Initialize a circle with given radius.
        
        :param radius: radius of the circle, may be zero.
        :raises ValueError: if radius is negative.
        """
        if radius < 0:
            raise ValueError("radius must be non-negative")
        self.radius = radius

    def add_area(self, circle: Circle) -> Circle:
        """Return a new circle whose area equals the combined
        area of this circle and another circle.
        Since area is pi*r**2, the radii of the 3 circles
        should form a Pythagorean triple (r1^2 + r2^2 = r3^2)
        """
        r1 = self.get_radius()
        r2 = circle.get_radius()
        # this is important, so show the operation in a rounded-box
        # on the Circle lifeline, or show it as a comment.
        r = math.hypot(r1, r2)
        # In a sequence diagram create a name for the new circle
        # so that you can show what is being returned.
        return Circle(r)

    def get_area(self) -> float:
        return math.pi*self.radius*self.radius
    
    def get_radius(self) -> float:
        return self.radius

    def __str__(self) -> str:
        return f"Circle({self.radius})"
    
    __repr__ = __str__


