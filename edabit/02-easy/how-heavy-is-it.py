"""
How Heavy Is It?
Given radius r and height h (in cm), calculate the mass of a cylinder when it's filled with water and the cylinder itself doesn't weigh anything. The desired output should be given in kg and rounded to two decimal places.

How to solve:

Calculate the volume of the cylinder.
Convert cm³ into dm³.
1dm³ = 1L, 1L is 1Kg.
Examples
weight(4, 10) ➞ 0.5

weight(30, 60) ➞ 169.65

weight(15, 10) ➞ 7.07
Notes
I recommend importing math.
If you get stuck on a challenge, find help in Resources.
"""

from edabit.Test import Test
from math import pi


def weight(r, h):
    volume = pi * r ** 2 * h
    dvolume = volume / 1000
    return round(dvolume, 2)


if __name__ == '__main__':
    Test.assert_equals(weight(4, 10), 0.5)
    Test.assert_equals(weight(30, 60), 169.65)
    Test.assert_equals(weight(15, 10), 7.07)
    Test.assert_equals(weight(20, 40), 50.27)
    Test.assert_equals(weight(100, 30), 942.48)
    Test.assert_equals(weight(200, 300), 37699.11)
    Test.assert_equals(weight(15, 23), 16.26)
    Test.assert_equals(weight(22, 44), 66.9)
