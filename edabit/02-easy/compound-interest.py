"""
Compound Interest
Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded monthly. What will be the value of your investment at the end of the 10 year period?

Create a function that accepts the principal p, the term in years t, the interest rate r, and the number of compounding periods per year n. The function returns the value at the end of term rounded to the nearest cent.

For the example above:

compound_interest(10000, 10, 0.06, 12) ➞ 18193.97
Note that the interest rate is given as a decimal and n=12 because with monthly compounding there are 12 periods per year. Compounding can also be done annually, quarterly, weekly, or daily.

Examples
compound_interest(100, 1, 0.05, 1) ➞ 105.0

compound_interest(3500, 15, 0.1, 4) ➞ 15399.26

compound_interest(100000, 20, 0.15, 365) ➞ 2007316.26
Notes
See the Resource for the interest formula and more information.
"""

from edabit.Test import Test


def compound_interest(p, t, r, n):
    return round((p*(1+(r/n))**(n*t)),2)

if __name__ == '__main__':
    Test.assert_equals(compound_interest(100, 1, 0.05, 1), 105.0)
    Test.assert_equals(compound_interest(3500, 15, 0.1, 4), 15399.26)
    Test.assert_equals(compound_interest(100000, 20, 0.15, 365), 2007316.26)