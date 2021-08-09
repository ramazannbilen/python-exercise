"""
Filter Strings from Array
Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.

Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]

filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]

filter_list(["Nothing", "here"]) ➞ []
Notes
Don't overthink this one.
"""

from edabit.Test import Test


def filter_list(l):
    #listt = [i for i in l if isinstance(i,int) == True]
    #return listt

    def abc(x):
        if isinstance(x,int) == True:           #long way
            return True
        else:
            return False
    son = filter(abc,l)
    bos= []
    for x in son:
        bos += [x]
    return bos



if __name__ == '__main__':
    Test.assert_equals(filter_list([1, 2, 3, "a", "b", 4]), [1, 2, 3, 4])
    Test.assert_equals(filter_list(["A", 1, "&amp", 0, -9, "Edabit"]), [1, 0, -9])
