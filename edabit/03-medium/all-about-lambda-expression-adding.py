"""All About Lambda Expressions: Adding
Write a function that returns a lambda expression, which adds n to its input

Examples
adds1 = adds_n(1)

adds1(3) ➞ 4
adds1(5.7) ➞ 6.7

adds10 = adds_n(10)

adds10(44) ➞ 54
adds10(20) ➞ 30
Notes
N/A"""

from edabit.Test import Test


def adds_n(n):
    return lambda x: x + n


adds1 = adds_n(1)
adds10 = adds_n(10)
adds5neg = adds_n(-5)
adds0 = adds_n(0)

Test.assert_equals(adds1(3), 4)
Test.assert_equals(adds1(5.7), 6.7)
Test.assert_equals(adds10(44), 54)
Test.assert_equals(adds10(20), 30)

Test.assert_equals(adds5neg(0), -5)
Test.assert_equals(adds5neg(77), 72)
Test.assert_equals(adds0(77), 77)
