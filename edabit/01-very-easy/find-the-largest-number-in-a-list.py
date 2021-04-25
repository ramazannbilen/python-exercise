"""
Find the Largest Number in a List
Create a function that takes a list of numbers. Return the largest number in the list.

Examples
findLargestNum([4, 5, 1, 3]) ➞ 5

findLargestNum([300, 200, 600, 150]) ➞ 600

findLargestNum([1000, 1001, 857, 1]) ➞ 1001
Notes
Expect either positive numbers or zero (there are no negative numbers).
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""

from edabit.Test import Test


def findLargestNum(nums):
    return max(nums)


if __name__ == '__main__':
    Test.assert_equals(findLargestNum([4, 5, 1, 3]), 5)
    Test.assert_equals(findLargestNum([13, 27, 18, 26]), 27)
    Test.assert_equals(findLargestNum([32, 35, 37, 39]), 39)
    Test.assert_equals(findLargestNum([1000, 1001, 857, 1]), 1001)
    Test.assert_equals(findLargestNum([27364, 837363, 736736, 73635]), 837363)
    Test.assert_equals(findLargestNum([30, 2, 40, 3]), 40)
    Test.assert_equals(findLargestNum([0, 1, 0, 0, 1]), 1)
