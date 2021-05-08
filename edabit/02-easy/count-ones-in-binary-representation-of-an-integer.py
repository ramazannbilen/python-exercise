"""
Count Ones in Binary Representation of Integer
Count the amount of ones in the binary representation of an integer. For example, since 12 is 1100 in binary, the return value should be 2.

Examples
count_ones(0) ➞ 0

count_ones(100) ➞ 3

count_ones(999) ➞ 8
Notes
The input will always be a valid integer (number).
"""

from edabit.Test import Test


def count_ones(num):
    number = bin(num)[2:]
    return number.count("1")

# def count_ones(num):
#     number = bin(num)[2:]
#     array = number.split("1")
#     return len(array) - 1


if __name__ == '__main__':
    Test.assert_equals(count_ones(12), 2)
    Test.assert_equals(count_ones(0), 0)
    Test.assert_equals(count_ones(100), 3)
    Test.assert_equals(count_ones(101), 4)
    Test.assert_equals(count_ones(999), 8)
    Test.assert_equals(count_ones(123456789), 16)
    Test.assert_equals(count_ones(1234567890), 12)
