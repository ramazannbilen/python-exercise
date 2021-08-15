"""
A Circle and Two Squares
Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.

Scale

Create a function, that takes an integer (radius of the circle) and returns the difference of the areas of the two squares.

Examples
square_areas_difference(5) ➞ 50

square_areas_difference(6) ➞ 72

square_areas_difference(7) ➞ 98
Notes
Use only positive integer parameters.
"""

from edabit.Test import Test


def square_areas_difference(r):
    return round(4 * (r ** 2) - (r * ((2) ** (1 / 2))) ** 2)  # absolute math


if __name__ == '__main__':
    Test.assert_equals(square_areas_difference(5), 50)
    Test.assert_equals(square_areas_difference(6), 72)
    Test.assert_equals(square_areas_difference(7), 98)
    Test.assert_equals(square_areas_difference(17), 578)
