# Question 1
class Rectangle:
    """ A rectangle with a width and height. """

    def __init__(self, w: float, h: float) -> None:
        """Create a new rectangle of width w and height h.

        >>> r = Rectangle(1.5, 2.7)
        >>> r.width
        1.5
        >>> r.height
        2.7
        """

        self.width = w
        self.height = h

    def area(self) -> float:
        """Return the area of this rectangle.

        >>> r = Rectangle(10.0, 20.0)
        >>> r.area()
        200.0
        """

        return self.width * self.height
