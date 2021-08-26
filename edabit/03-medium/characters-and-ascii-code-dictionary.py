"""Characters and ASCII Code Dictionary
Write a function that transforms a list of characters into a list of dictionaries, where:

The keys are the characters themselves.
The values are the ASCII codes of those characters.
Examples
to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]

to_dict(["^"]) ➞ [{"^": 94}]

to_dict([]) ➞ []
Notes
N/A
"""

from edabit.Test import Test

def to_dict(lst):
    lst2 = []
    for i in lst:
        lst2.append({i:ord(i)})
    return lst2


Test.assert_equals(to_dict(["a", "b", "c"]), [{"a": 97}, {"b": 98}, {"c": 99}])
Test.assert_equals(to_dict(["!", ".", "?"]), [{"!": 33}, {".": 46}, {"?": 63}])
Test.assert_equals(to_dict(["^"]), [{"^": 94}])
Test.assert_equals(to_dict([" "]), [{" ": 32}])
Test.assert_equals(to_dict([]), [])