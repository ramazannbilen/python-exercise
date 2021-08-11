"""
Find the Missing Number
Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.

Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5

missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10

missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
Notes
The list of numbers will be unsorted (not in order).
Only one number will be missing.
"""

from edabit.Test import Test

def missing_num(lst):
    misnum = [i for i in range(1,11) if i not in lst]
    return misnum[0]


if __name__ == '__main__':
    Test.assert_equals(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]), 5)
    Test.assert_equals(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]), 10)
    Test.assert_equals(missing_num([7, 2, 3, 9, 4, 5, 6, 8, 10]), 1)
    Test.assert_equals(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]), 7)
    Test.assert_equals(missing_num([1, 7, 2, 4, 8, 10, 5, 6, 9]), 3)