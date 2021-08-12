"""
Clone a List
The Code tab has code which attempts to add a clone of a list to itself. There is no error message, but the results are not as intended. Can you fix the code?

Examples
clone([1, 1]) ➞ [1, 1, [1, 1]]

clone([1, 2, 3]) ➞ [1, 2, 3, [1, 2, 3]]

clone(["x", "y"]) ➞ ["x", "y", ["x", "y"]]
Notes
N/A
"""

from edabit.Test import Test

def clone(lst):
    lst.append([i for i in lst])
    return lst

if __name__ == '__main__':
    Test.assert_equals(clone([1, 1]), [1, 1, [1, 1]])
    Test.assert_equals(clone(["a", "b", "c"]), ["a", "b", "c", ["a", "b", "c"]])
    Test.assert_equals(clone([]), [[]])