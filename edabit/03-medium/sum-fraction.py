"""Sum Fractions
Create a function that takes a list containing nested lists as an argument. Each sublist has 2 elements. The first element is the numerator and the second element is the denominator. Return the sum of the fractions rounded to the nearest whole number.

Examples
sum_fractions([[18, 13], [4, 5]]) ➞ 2

sum_fractions([[36, 4], [22, 60]]) ➞ 9

sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]) ➞ 11
Notes
Your result should be a number not string."""

from edabit.Test import Test


def sum_fractions(lst):
    def kesir(list):
        return list[0] / list[1]

    sum = 0
    for i in lst:
        sum += kesir(i)
    return round(sum)

Test.assert_equals(sum_fractions([[36, 4], [22, 60]]), 9)
Test.assert_equals(sum_fractions([[-11, 12], [18, 13], [4, 5]]), 1)
Test.assert_equals(sum_fractions([[11, 12], [18, 13], [4, 5]]), 3)
Test.assert_equals(sum_fractions([[18, 13], [4, 5]]), 2)
Test.assert_equals(sum_fractions([[41, 14], [10, 91]]), 3)
Test.assert_equals(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]), 11)
