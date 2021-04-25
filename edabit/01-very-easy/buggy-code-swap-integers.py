"""
Buggy Code (Part 7)
Mubashir wants to swap two given numbers!

It is not returning the right values. Can you help him fix it?

a = 100
b = 200
a, b = swap(a, b)
print(a, b) # Should print out "200, 100", but the function prints out "100, 100"
Examples
swap(100, 200) ➞ [200, 100]

swap(44, 33) ➞ [33, 44]

swap(21, 12) ➞ [12, 21]
"""

from edabit.Test import Test


def swap(a, b):
    temp = a   # first code was: a=b,b=a
    a = b
    b = temp
    return [a, b]

if __name__ == '__main__':
    Test.assert_equals(swap(100, 200), [200, 100])
    Test.assert_equals(swap(44, 33), [33, 44])
    Test.assert_equals(swap(21, 12), [12, 21])
    Test.assert_equals(swap(10, 20), [20, 10])
