"""
Even Number Generator
Using list comprehensions, create a function that finds all even numbers from 1 to the given number.

Examples
find_even_nums(8) ➞ [2, 4, 6, 8]

find_even_nums(4) ➞ [2, 4]

find_even_nums(2) ➞ [2]
Try to use list comprehensions in your solution. Here's an example:

vals = [expression
  for value in collection
    if condition]
This is equivalent to:

vals = []
for value in collection:
  if condition:
    vals.append(expression)
Notes
Try to use list comprehensions instead of logic.
If there are no even numbers, return an empty list.
"""

from edabit.Test import Test


def find_even_nums(num):
    listt = [(i + 1) for i in range(num) if (i + 1) % 2 == 0]   # list comprehension
    return listt


if __name__ == '__main__':
    Test.assert_equals(find_even_nums(4), [2, 4])
    Test.assert_equals(find_even_nums(8), [2, 4, 6, 8])
    Test.assert_equals(find_even_nums(2), [2])
    Test.assert_equals(find_even_nums(1), [])
    Test.assert_equals(find_even_nums(9), [2, 4, 6, 8])
    Test.assert_equals(find_even_nums(11), [2, 4, 6, 8, 10])
