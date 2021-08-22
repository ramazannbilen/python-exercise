"""
How Many Solutions Does This Quadratic Have?
A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for real values of x. Given a, b and c, you should return the number of solutions to the equation.

Examples
solutions(1, 0, -1) ➞ 2
// x² - 1 = 0 has two solutions (x = 1 and x = -1).

solutions(1, 0, 0) ➞ 1
// x² = 0 has one solution (x = 0).

solutions(1, 0, 1) ➞ 0
// x² + 1 = 0 has no real solutions.
Notes
You do not have to calculate the solutions, just return how many there are.
a will always be non-zero.
"""

from edabit.Test import Test

def solutions(a, b, c):
    if b**2-4*a*c > 0:
        return 2
    elif b**2-4*a*c < 0:
        return 0
    else:
        return 1
    # info: b^2 - 4ac is the solution formula of the quadratic functions.

if __name__ == '__main__':
    Test.assert_equals(solutions(1, 0, -1), 2)
    Test.assert_equals(solutions(1, 0, 0), 1)
    Test.assert_equals(solutions(1, 0, 1), 0)
    Test.assert_equals(solutions(200, 420, 800), 0)
    Test.assert_equals(solutions(200, 420, -800), 2)
    Test.assert_equals(solutions(1000, 1000, 0), 2)
    Test.assert_equals(solutions(10000, 400, 4), 1)