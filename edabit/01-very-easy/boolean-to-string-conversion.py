"""
Boolean to String Conversion
Create a function that takes a boolean variable flag and returns it as a string.

Examples
bool_to_string(True) ➞ "True"

bool_to_string(False) ➞ "False"
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""

from edabit.Test import Test


def bool_to_string(flag):
    if flag == True:
        return "True"
    else:
        return "False"


if __name__ == '__main__':
    Test.assert_equals(bool_to_string(True), "True")
    Test.assert_equals(bool_to_string(False), "False")
