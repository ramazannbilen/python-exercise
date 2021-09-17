"""
Designing Rugs
Write a function that accepts the width and height (m, n) and an optional proc s and generates a list with m elements. Each element is a string consisting of either:

The default character (hash #) repeating n times (if no proc is given).
The character passed in through the proc repeating n times.
Examples
make_rug(3, 5) ➞ [
  "#####",
  "#####",
  "#####"
]

make_rug(3, 5, '$')  ➞ [
  "$$$$$",
  "$$$$$",
  "$$$$$"
]

make_rug(2, 2, 'A')  ➞ [
  "AA"
  "AA"
]
Notes
You can set a value for the parameter when creating the function e.g. def func(x = 3)
"""

from edabit.Test import Test


def make_rug(m, n, s="#"):
    lst = [s * n for i in range(m)]
    # for i in range(0, m):
    #     lst.append(s * n)
    return lst


Test.assert_equals(make_rug(3, 5), [
    "#####",
    "#####",
    "#####"
])

Test.assert_equals(make_rug(3, 5, '$'), [
    "$$$$$",
    "$$$$$",
    "$$$$$"
])

Test.assert_equals(make_rug(2, 2, 'A'), [
    "AA",
    "AA"
])

Test.assert_equals(make_rug(3, 1, 'b'), [
    "b",
    "b",
    "b"
])

Test.assert_equals(make_rug(2, 1, 'bcb'), [
    "bcb",
    "bcb"
])
