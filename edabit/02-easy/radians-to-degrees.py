"""
Radians to Degrees
Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.

Examples
radians_to_degrees(1) ➞ 57.3

radians_to_degrees(20) ➞ 1145.9

radians_to_degrees(50) ➞ 2864.8
Notes
The number π can be loaded from the math module with from math import pi
"""

from edabit.Test import Test
from math import pi


def radians_to_degrees(rad):
    return round(rad / pi * 180, 1)  #this method rounds number round(number,index after comma)


if __name__ == '__main__':
    Test.assert_equals(radians_to_degrees(1), 57.3)
    Test.assert_equals(radians_to_degrees(5), 286.5)
    Test.assert_equals(radians_to_degrees(7), 401.1)
    Test.assert_equals(radians_to_degrees(60), 3437.7)
    Test.assert_equals(radians_to_degrees(100), 5729.6)
    Test.assert_equals(radians_to_degrees(180), 10313.2)
