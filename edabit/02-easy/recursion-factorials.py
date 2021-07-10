"""
Recursion: Factorials
Write a function that calculates the factorial of a number recursively.

Examples
factorial(5) ➞ 120

factorial(3) ➞ 6

factorial(1) ➞ 1

factorial(0) ➞ 1
Notes
N/A
"""

from edabit.Test import Test


def factorial(n):
    """fact = 1
    for k in range(2, (n + 1)):         first alternative
        fact *= k
    return fact"""
    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n - 1))


if __name__ == '__main__':
    Test.assert_equals(factorial(5), 120)
    Test.assert_equals(factorial(3), 6)
    Test.assert_equals(factorial(1), 1)
    Test.assert_equals(factorial(0), 1)
