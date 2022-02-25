"""
Geometry 3: Perimeter of a Triangle
Write a function that takes the coordinates of three points in the form of a 2d array and returns the perimeter of the triangle. The given points are the vertices of a triangle on a two-dimensional plane.

Examples
perimeter([[15, 7], [5, 22], [11, 1]]) ➞ 47.08

perimeter([[0, 0], [0, 1], [1, 0]]) ➞ 3.42

perimeter([[-10, -10], [10, 10 ], [-10, 10]]) ➞ 68.28
Notes
The given points always create a triangle.
The numbers in the argument array can be positive or negative.
Output should have 2 decimal places
This challenge is easier than it looks.
"""

from edabit.Test import Test


def perimeter(lst):
    x1 = abs(lst[0][0]-lst[1][0])**2 + abs(lst[0][1]-lst[1][1])**2
    x2 = abs(lst[0][0]-lst[2][0])**2 + abs(lst[0][1]-lst[2][1])**2
    x3 = abs(lst[1][0]-lst[2][0])**2 + abs(lst[1][1]-lst[2][1])**2

    return round(x1**(1/2) + x2**(1/2) + x3**(1/2),2)

Test.assert_equals(perimeter([[0, 0], [1, 0], [0, 1]]), 3.41)
Test.assert_equals(perimeter([[15, 7], [5, 22], [11, 1]]), 47.08)
Test.assert_equals(perimeter([[7, 6], [0, 11], [0, -3]]), 34.00)
Test.assert_equals(perimeter([[-10, -10], [10, 10], [-10, 10]]), 68.28)
Test.assert_equals(perimeter([[3, 4], [4, 3], [4, 5]]), 4.83)
Test.assert_equals(perimeter([[-10, -20], [-30, -40], [-50, -60]]), 113.14)
Test.assert_equals(perimeter([[382, 894], [389, 312], [500, 993]]), 1426.06)