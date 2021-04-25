"""
String to Integer and Vice Versa
Write two functions:

to_int() : A function to convert a string to an integer.
to_str() : A function to convert an integer to a string.
Examples
to_int("77") ➞ 77

to_int("532") ➞ 532

to_str(77) ➞ "77"

to_str(532) ➞ "532"
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""

from edabit.Test import Test


def to_int(txt):
    return int(txt)

def to_str(num):
    return str(num)


if __name__ == '__main__':
    Test.assert_equals(to_int("37"), 37)
    Test.assert_equals(to_int("113"), 113)
    Test.assert_equals(to_int("5"), 5)
    Test.assert_equals(to_int("5231"), 5231)
    Test.assert_equals(to_str(37), "37")
    Test.assert_equals(to_str(113), "113")
    Test.assert_equals(to_str(5), "5")
    Test.assert_equals(to_str(5231), "5231")
