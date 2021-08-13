"""
Length of Number
Create a function that takes a number num and returns its length.

Examples
number_length(10) ➞ 2

number_length(5000) ➞ 4

number_length(0) ➞ 1
Notes
The use of the len() function is prohibited.
"""

from edabit.Test import Test


def number_length(num):
    st = str(num)
    count = 0
    for i in st:
        count += 1
    return count


if __name__ == '__main__':
    Test.assert_equals(number_length(10), 2)
    Test.assert_equals(number_length(5000), 4)
    Test.assert_equals(number_length(0), 1)
    Test.assert_equals(number_length(4039182), 7)
    Test.assert_equals(number_length(9999999999999999), 16)
    Test.assert_equals(number_length(1), 1)
    Test.assert_equals(number_length(777777777777777777777777777777), 30)
