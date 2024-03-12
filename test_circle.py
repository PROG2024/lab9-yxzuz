"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""

# TODO write 3 tests as described above
from circle import Circle
import unittest
import math
class CircledTest(unittest.TestCase):
    # def setUp(self):
    #     """Create an auction before each test."""
    #     self.circle = Circle()

    def test_add_area(self):
        c1 = Circle(2)
        c2 = Circle(4)
        new_circle = c1.add_area(c2)
        total_area = c1.get_area()+c2.get_area()
        # print(c1.get_area() + c2.get_area())
        self.assertAlmostEqual(total_area,new_circle.get_area()) # check area
        self.assertAlmostEqual(math.sqrt((c1.get_radius())**2 + (c2.get_radius())**2),new_circle.get_radius())
        # print(new_circle.get_area())

    def test_edge_area(self):
        c1 = Circle(0)
        c2 = Circle(4)
        new_circle = c1.add_area(c2)
        total_area = c1.get_area()+c2.get_area()
        self.assertAlmostEqual(total_area,new_circle.get_area()) # check area
        self.assertAlmostEqual(math.sqrt((c1.get_radius())**2 + (c2.get_radius())**2),new_circle.get_radius())