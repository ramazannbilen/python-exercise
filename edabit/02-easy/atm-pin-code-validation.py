"""
ATM PIN Code Validation
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. Your task is to create a function that takes a string and returns True if the PIN is valid and False if it's not.

Examples
is_valid_PIN("1234") ➞ True

is_valid_PIN("12345") ➞ False

is_valid_PIN("a234") ➞ False

is_valid_PIN("") ➞ False
Notes
Some test cases contain special characters.
Empty strings must return False.
"""

from edabit.Test import Test


def is_valid_PIN(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isnumeric() == True:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    Test.assert_equals(is_valid_PIN("1234"), True)
    Test.assert_equals(is_valid_PIN("12345"), False)
    Test.assert_equals(is_valid_PIN("a234"), False)
    Test.assert_equals(is_valid_PIN(""), False)
    Test.assert_equals(is_valid_PIN("%234"), False)
    Test.assert_equals(is_valid_PIN("`234"), False)
    Test.assert_equals(is_valid_PIN("@234"), False)
    Test.assert_equals(is_valid_PIN("#234"), False)
    Test.assert_equals(is_valid_PIN("$234"), False)
    Test.assert_equals(is_valid_PIN("*234"), False)
    Test.assert_equals(is_valid_PIN("5678"), True)
    Test.assert_equals(is_valid_PIN("^234"), False)
    Test.assert_equals(is_valid_PIN("(234"), False)
    Test.assert_equals(is_valid_PIN(")234"), False)
    Test.assert_equals(is_valid_PIN("123456"), True)
    Test.assert_equals(is_valid_PIN("-234"), False)
    Test.assert_equals(is_valid_PIN("_234"), False)
    Test.assert_equals(is_valid_PIN("+234"), False)
    Test.assert_equals(is_valid_PIN("=234"), False)
    Test.assert_equals(is_valid_PIN("?234"), False)