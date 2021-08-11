"""
Triangular Number Sequence
This Triangular Number Sequence is generated from a pattern of dots that form a triangle. The first 5 numbers of the sequence, or dots, are:

1, 3, 6, 10, 15
This means that the first triangle has just one dot, the second one has three dots, the third one has 6 dots and so on.

Write a function that returns the number of dots when given its corresponding triangle number of the sequence.

Examples
triangle(1) ➞ 1

triangle(6) ➞ 21

triangle(215) ➞ 23220
Notes
Check the Resources for info on triangular number sequence.
"""

from edabit.Test import Test

def triangle(n):
    return n*(n+1)/2

if __name__ == '__main__':
    Test.assert_equals(triangle(1), 1)
    Test.assert_equals(triangle(2), 3)
    Test.assert_equals(triangle(3), 6)
    Test.assert_equals(triangle(8), 36)
    Test.assert_equals(triangle(2153), 2318781)