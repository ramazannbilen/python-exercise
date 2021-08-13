"""
Geometry 1: Length of Line Segment
Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.

Examples
line_length([15, 7], [22, 11]) ➞ 8.06

line_length([0, 0], [0, 0]) ➞ 0

line_length([0, 0], [1, 1]) ➞ 1.41
Notes
The order of the given numbers is X, Y.
This challenge is easier than it looks.
Round your result to two decimal places.
"""

from edabit.Test import Test

import math
def line_length(dot1, dot2):
    # xaxis = [dot1[0], dot2[0]]  # pythagorean
    # yaxis = [dot1[1], dot2[1]]
    xlong = abs(dot1[0] - dot2[0])
    ylong = abs(dot1[1] - dot2[1])
    return round((xlong ** 2 + ylong ** 2) ** (1 / 2), 2)


if __name__ == '__main__':
    Test.assert_equals(line_length([15, 7], [22, 11]), 8.06)
    Test.assert_equals(line_length([0, 0], [0, 0]), 0)
    Test.assert_equals(line_length([0, 0], [1, 1]), 1.41)
    Test.assert_equals(line_length([30, 10], [13, -5]), 22.67)