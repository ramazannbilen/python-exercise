"""
The Reverser!
The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.

Examples
reverse("Hello World") ➞ "DLROw OLLEh"

reverse("ReVeRsE") ➞ "eSrEvEr"

reverse("Radar") ➞ "RADAr"
Notes
There will be no punctuation in any of the test cases.
"""

from edabit.Test import Test


def reverse(txt):
    txt = txt[::-1].swapcase()

    return txt


if __name__ == '__main__':
    Test.assert_equals(reverse("Hello World"), "DLROw OLLEh")
    Test.assert_equals(reverse("ReVeRsE"), "eSrEvEr")
    Test.assert_equals(reverse(""), "")
    Test.assert_equals(reverse("Radar"), "RADAr")
