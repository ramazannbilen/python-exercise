"""
Volume of a Cone
Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.

Volume of a Cone Image

Examples
cone_volume(3, 2) ➞ 12.57

cone_volume(15, 6) ➞ 565.49

cone_volume(18, 0) ➞ 0
Notes
Return approximate answer by rounding the answer to the nearest hundredth.
Use Python's math.pi constant or equivalent, don't fall for 3.14 ;-)
If the cone has no volume, return 0.
"""
import math
from edabit.Test import Test


def cone_volume(h, r):
    vol = (1 / 3) * math.pi * (r ** 2) * h
    return round(vol,2)

if __name__ == '__main__':
    Test.assert_equals(cone_volume(3, 2), 12.57)
    Test.assert_equals(cone_volume(15, 6), 565.49)
    Test.assert_equals(cone_volume(18, 0), 0)
    Test.assert_equals(cone_volume(100, 2), 418.88)
    Test.assert_equals(cone_volume(1, 1), 1.05)
    Test.assert_equals(cone_volume(0, 30), 0)
