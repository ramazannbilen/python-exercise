"""
Recursion: Sum
Write a function that finds the sum of the first n natural numbers. Make your function recursive.

Examples
sum_numbers(5) ➞ 15
# 1 + 2 + 3 + 4 + 5 = 15

sum_numbers(1) ➞ 1

sum_numbers(12) ➞ 78
Notes
Assume the input number is always positive.
Check the Resources tab for info on recursion.
"""

from edabit.Test import Test


def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return (n + sum_numbers(n - 1))


if __name__ == '__main__':
    Test.assert_equals(sum_numbers(1), 1)
    Test.assert_equals(sum_numbers(5), 15)
    Test.assert_equals(sum_numbers(7), 28)
    Test.assert_equals(sum_numbers(10), 55)
    Test.assert_equals(sum_numbers(12), 78)
    Test.assert_equals(sum_numbers(15), 120)
    Test.assert_equals(sum_numbers(20), 210)
    Test.assert_equals(sum_numbers(100), 5050)
