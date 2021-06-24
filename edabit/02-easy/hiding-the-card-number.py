"""
Hiding the Card Number
Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.

Examples
card_hide("1234123456785678") ➞ "************5678"

card_hide("8754456321113213") ➞ "************3213"

card_hide("35123413355523") ➞ "**********5523"
Examples
Ensure you return a string.
The length of the string must remain the same as the input.
"""

from edabit.Test import Test


def card_hide(card):
    c2 = str(card)
    for i in range(len(c2)):
        c2 = c2.replace(c2[i], "*")
    return c2[:-4] + card[-4:]


if __name__ == '__main__':
    Test.assert_equals(card_hide("1234123456785678"), "************5678")
    Test.assert_equals(card_hide("8754456321113213"), "************3213")
    Test.assert_equals(card_hide("35123413355523"), "**********5523")
