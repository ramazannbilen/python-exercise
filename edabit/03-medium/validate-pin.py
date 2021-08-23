"""Validate Pin
Create a function to test if a string is a valid pin or not.

A valid pin has:

Exactly 4 or 6 characters.
Only numerical characters (0-9).
No whitespace.
Examples
valid("1234") ➞ True

valid("45135") ➞ False

valid("89abc1") ➞ False

valid("900876") ➞ True

valid(" 4983") ➞ False
Notes
Empty strings should return False when tested."""

from edabit.Test import Test


def valid(txt):
    if txt.isnumeric() == True and (len(txt) == 4 or len(txt) == 6):
        return True
    else:
        return False


tests = [
    ['123456', True],
    ['4512a5', False],
    ['', False],
    ['21904', False],
    ['9451', True],
    ['213132', True],
    [' 4520', False],
    ['15632 ', False],
    ['000000', True]
]

for test in tests:
    Test.assert_equals(valid(test[0]), test[1])
