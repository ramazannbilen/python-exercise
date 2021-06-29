"""
Let's Fuel Up!
A vehicle needs 10 times the amount of fuel than the distance it travels. However, it must always carry a minimum of 100 fuel before setting off.

Create a function which calculates the amount of fuel it needs, given the distance.

Examples
calculate_fuel(15) ➞ 150

calculate_fuel(23.5) ➞ 235

calculate_fuel(3) ➞ 100
Notes
Distance will be a number greater than zero.
Return 100 if the calculated fuel turns out to be less than 100.
"""

from edabit.Test import Test


def calculate_fuel(n):
    if n < 10:
        return 100
    else:
        return n * 10


if __name__ == '__main__':
    Test.assert_equals(calculate_fuel(15), 150)
    Test.assert_equals(calculate_fuel(23), 230)
    Test.assert_equals(calculate_fuel(10), 100)
    Test.assert_equals(calculate_fuel(3), 100)
    Test.assert_equals(calculate_fuel(23.5), 235)
    Test.assert_equals(calculate_fuel(3.14), 100)
    Test.assert_equals(calculate_fuel(9.99999), 100)
    Test.assert_equals(calculate_fuel(822315322), 8223153220)
    Test.assert_equals(calculate_fuel(12345.6789), 123456.789)
    Test.assert_equals(calculate_fuel(31.41), 314.1)
