"""
Flip the Boolean
Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.

Examples
reverse(True) ➞ False

reverse(False) ➞ True

reverse(0) ➞ "boolean expected"

reverse(None) ➞ "boolean expected"
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""

from edabit.Test import Test


def reverse(arg):
    #if arg == True:
    #    return False
    #elif arg == False:
    #    return arg
    #else:
    #    return "boolean expected"

    if type(arg) == bool:
        if arg == False:
            return True
        elif arg == True:
            return False
    else:
        return "boolean expected"



if __name__ == '__main__':
    Test.assert_equals(reverse(False), True)
    Test.assert_equals(reverse(True), False)
    Test.assert_equals(reverse(0), "boolean expected")
    Test.assert_equals(reverse(None), "boolean expected")
    Test.assert_equals(reverse(""), "boolean expected")
    Test.assert_equals(reverse({}), "boolean expected")
