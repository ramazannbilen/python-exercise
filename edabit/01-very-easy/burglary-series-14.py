"""
Burglary Series (14): Adjectives Total
You call your spouse in anger and a "little" argument takes place. Count the total amount of adjectives used. Given a dictionary of adjectives, return the total amount of adjectives used.

Examples
total_amount_adjectives({ "a": "moron" }) ➞ 1

total_amount_adjectives({ "a": "idiot", "b": "idiot", "c": "idiot" }) ➞ 3

total_amount_adjectives({ "a": "moron", "b": "scumbag", "c": "moron", d: "dirtbag" }) ➞ 4
Notes
The dictionary will never be empty.
"""

from edabit.Test import Test
import random

obj = {'a': "moron"}
obj2 = {'a': "moron", 'b': "scumbag", 'c': "moron", 'd': "dirtbag"}
obj3 = {'b': "scumbag", 'c': "moron", 'd': "dirtbag"}
rand = random.randint(10, 20)
dynamic = {i: j for i, j in list(map(lambda x: (chr(65 + x), x), list(range(rand))))}


def total_amount_adjectives(dct):
    return len(dct)

if __name__ == '__main__':
    Test.assert_equals(total_amount_adjectives(obj), 1)
    Test.assert_equals(total_amount_adjectives(obj2), 4)
    Test.assert_equals(total_amount_adjectives(obj3), 3)
    Test.assert_equals(total_amount_adjectives(dynamic), rand)
