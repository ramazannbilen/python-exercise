"""
Probabilities (Part 1)
Given a list of numbers and a value n, write a function that returns the probability of choosing a number greater than or equal to n from the list. The probability should be expressed as a percentage, rounded to one decimal place.

Examples
probability([5, 1, 8, 9], 6) ➞ 50.0

probability([7, 4, 17, 14, 12, 3], 16) ➞ 16.7

probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6) ➞ 70.0
Notes
Precent probability of event = 100 * (num of favourable outcomes) / (total num of possible outcomes)
The numbers in the list are uniformly distributed, and have an equal chance of being chosen.
"""

from edabit.Test import Test

def probability(lst, n):
    greater = [i for i in lst if i >= n]
    return round((len(greater)/len(lst)*100),1)

if __name__ == '__main__':
    Test.assert_equals(probability([14, 19, 2, 6], 12), 50.0)
    Test.assert_equals(probability([11, 10, 9, 18, 16, 18, 4, 3, 5], 13), 33.3)
    Test.assert_equals(probability([2, 13, 1, 11, 6, 9, 11, 14, 3], 15), 0.0)
    Test.assert_equals(probability([11, 6, 17, 2, 1, 16, 20, 15], 7), 62.5)
    Test.assert_equals(probability([12, 15, 12, 8, 20, 16, 1], 1), 100.0)
    Test.assert_equals(probability([15, 8, 12, 1, 11, 4], 4), 83.3)
    Test.assert_equals(probability([14, 11, 16, 3, 13, 14, 3], 8), 71.4)
    Test.assert_equals(probability([1, 4, 18, 19, 15, 3, 3, 11], 23), 0.0)
    Test.assert_equals(probability([9, 8, 17, 13, 17], 8), 100.0)
    Test.assert_equals(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6), 70.0)
    Test.assert_equals(probability([15, 4, 6, 11, 11, 17, 9, 16, 7, 4, 5, 10], 12), 25.0)
    Test.assert_equals(probability([7, 1, 5, 7, 15, 15, 16, 14], 2), 87.5)
    Test.assert_equals(probability([11, 4, 6, 7, 14, 4, 4], 8), 28.6)
    Test.assert_equals(probability([10, 10, 3, 18, 14, 1, 2, 19, 17, 2, 4, 11, 18, 6, 3], 11), 40.0)