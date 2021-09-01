"""Sastry Numbers
In this challenge, you have to establish if a given integer n is a Sastry number. If the number resulting from the concatenation of an integer n with its successor is a perfect square, then n is a Sastry Number.

Given a positive integer n, implement a function that returns True if n is a Sastry number, or False if it's not.

Examples
is_sastry(183) ➞ True
# Concatenation of n and its successor = 183184
# 183184 is a perfect square (428 ^ 2)

is_sastry(184) ➞ False
# Concatenation of n and its successor = 184185
# 184185 is not a perfect square

is_sastry(106755) ➞ True
# Concatenation of n and its successor = 106755106756
# 106755106756 is a perfect square (326734 ^ 2)
Notes
A perfect square is a number with a square root equals to a whole integer.
You can expect only valid positive integers greater than 0 as input, without exceptions to handle. Zero is a perfect square, but the concatenation 00 isn't considered as a valid result to check."""

from edabit.Test import Test


def is_sastry(n):
    return

Test.assert_equals(is_sastry(183), True)
Test.assert_equals(is_sastry(184), False)
Test.assert_equals(is_sastry(106755), True)
Test.assert_equals(is_sastry(129987253440921), False)
Test.assert_equals(is_sastry(157175907513603), True)
Test.assert_equals(is_sastry(206611570247935), True)
Test.assert_equals(is_sastry(338752188230098), False)
Test.assert_equals(is_sastry(433610247875715), True)
Test.assert_equals(is_sastry(652333983478884), False)
Test.assert_equals(is_sastry(718717107443715), True)
Test.assert_equals(is_sastry(752199872453889), False)
Test.assert_equals(is_sastry(786704531939448), True)
