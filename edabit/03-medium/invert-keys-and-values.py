"""Invert Keys and Values
Write a function that inverts the keys and values of a dictionary.

Examples
invert({ "z": "q", "w": "f" })
➞ { "q": "z", "f": "w" }

invert({ "a": 1, "b": 2, "c": 3 })
➞ { 1: "a", 2: "b", 3: "c" }

invert({ "zebra": "koala", "horse": "camel" })
➞ { "koala": "zebra", "camel": "horse" }
Notes
N/A"""
from edabit.Test import Test


def invert(dct):
    # dict = {value : key for key,value in dct.items()}
    a = dict(zip(dct.values(), dct.keys()))
    return a
Test.assert_equals(invert({"a": 1, "b": 2, "c": 3}), {1: "a", 2: "b", 3: "c"})
Test.assert_equals(invert({"z": "q", "w": "f"}), {"q": "z", "f": "w"})
Test.assert_equals(invert({"zebra": "koala", "horse": "camel"}), {"koala": "zebra", "camel": "horse"})