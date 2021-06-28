"""
Find the Odd Integer
Create a function that takes a list and finds the integer which appears an odd number of times.

Examples
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1

find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5

find_odd([10]) ➞ 10
Notes
There will always only be one integer that appears an odd number of times.
"""

from edabit.Test import Test


def find_odd(lst):
    for i in range(len(lst)):
        count = 0
        for k in range(len(lst)):
            if lst[i] == lst[k]:           # remember to use "for loop" as nested when you want to check all elements of a list eachother
                count += 1
        if (count %2 != 0):
            return lst[i]


if __name__ == '__main__':
    Test.assert_equals(find_odd([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
    Test.assert_equals(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1)
    Test.assert_equals(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5)
    Test.assert_equals(find_odd([10]), 10)
    Test.assert_equals(find_odd([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10)
    Test.assert_equals(find_odd([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1)
