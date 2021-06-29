"""
Unpacking Lists
You can assign variables from lists like this:

lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]

print(first) ➞ outputs 1
print(middle) ➞ outputs [2, 3, 4, 5]
print(last) ➞ outputs 6
With Python 3, you can assign variables from lists in a much more succinct way. Create variables first, middle and last from the given list using destructuring assignment (check the Resources tab for some examples), where:

first  ➞ 1

middle ➞ [2, 3, 4, 5]

last ➞ 6
Your task is to unpack the list writeyourcodehere into three variables, being first, middle, and last, with middle being everything in between the first and last element. Then print all three variables.

Notes
Your solution should be just one line of code.
If your solution is longer than one line of code, please review the Resources tab.
"""

from edabit.Test import Test

first, *middle, last = [1, 2, 3, 4, 5, 6]
print(first)
print(middle)
print(last)

if __name__ == '__main__':
    Test.assert_equals(first, 1, 'Variable first does not equal 1')
    Test.assert_equals(middle, [2, 3, 4, 5], 'Variable middle does not equal [2, 3, 4, 5]')
    Test.assert_equals(last, 6, 'Variable last does not equal 6')
