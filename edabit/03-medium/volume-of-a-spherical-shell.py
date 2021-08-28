"""Volume of a Spherical Shell
The volume of a spherical shell is the difference between the enclosed volume of the outer sphere and the enclosed volume of the inner sphere:

Volume of Inner Sphere Formula

Create a function that takes r1 and r2 as arguments and returns the volume of a spherical shell rounded to the nearest thousandth.

Spherical Shell Image

Examples
vol_shell(3, 3) ➞ 0

vol_shell(7, 2) ➞ 1403.245

vol_shell(3, 800) ➞ 2144660471.753
Notes
The inputs are always positive numbers. r1 could be the inner radius or the outer radius, don't return a negative number."""

from math import pi
from edabit.Test import Test


def vol_shell(r1, r2):
    return round(abs(r1 ** 3 - r2 ** 3) * (pi * 4) / 3, 3)

Test.assert_equals(vol_shell(17, 36), 174852.67)
Test.assert_equals(vol_shell(3, 4), 154.985)
Test.assert_equals(vol_shell(1, 90), 3053623.87)
Test.assert_equals(vol_shell(12.5, 19), 20549.681)
Test.assert_equals(vol_shell(3, 800), 2144660471.753)
Test.assert_equals(vol_shell(16.128, 16.256), 421.719)
Test.assert_equals(vol_shell(3, 3), 0)
Test.assert_equals(vol_shell(4, 3), 154.985)
Test.assert_equals(vol_shell(36, 17), 174852.67)
Test.assert_equals(vol_shell(18, 96), 3681544.466)
Test.assert_equals(vol_shell(1, 7), 1432.566)
Test.assert_equals(vol_shell(7, 2), 1403.245)
Test.assert_equals(vol_shell(100, 50), 3665191.429)
Test.assert_equals(vol_shell(40, 36), 72650.377)
