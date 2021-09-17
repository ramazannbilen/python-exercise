"""
Format IX: Unpacking Lists
For each challenge of this series you do not need to submit a function. Instead, you need to submit a template string that can be formatted in order to get a certain outcome.

Write three lists and a template string according to the following example. Notice the keyword argument elem:

Example
lst1 = [yourlisthere]
lst2 = [yourlisthere]
lst3 = [yourlisthere]
template = "yourtemplatestringhere"

template.format(*lst1, elem="friends") ➞ "My friends are: John, Joe and Jack."
template.format(*lst2, elem="loves") ➞ "My loves are: E, da and bit."
template.format(*lst3, elem="pokemon") ➞ "My pokemon are: Metapod, Magikarp and Unown."
Tips
The elements of a list can be unpacked and passed to .format() as positional arguments using the star operator *:

names = ["Mary", "May"]
"{} and {}.".format(*names) ➞ "Mary and May."
Notes
Submit a string, not a function.
Do not change the names of the variables template, lst1, lst2 and lst3.
You can find all the exercises in this series over here.
"""

from edabit.Test import Test

lst1 = ["My", "John, Joe and Jack."]
lst2 = ["My", "E, da and bit."]
lst3 = ["My", "Metapod, Magikarp and Unown."]

template = "{} {elem} are: {}"

Test.assert_equals(template.format(*lst1, elem="friends"), "My friends are: John, Joe and Jack.")
Test.assert_equals(template.format(*lst2, elem="loves"), "My loves are: E, da and bit.")
Test.assert_equals(template.format(*lst3, elem="pokemon"), "My pokemon are: Metapod, Magikarp and Unown.")
