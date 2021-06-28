"""
Find the Discount
Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.


Examples
dis(1500, 50) ➞ 750

dis(89, 20) ➞ 71.2

dis(100, 75) ➞ 25
"""

from edabit.Test import Test


def dis(price, discount):
    return round((price - (price*discount/100)),2)

if __name__ == '__main__':
    Test.assert_equals(dis(100, 75), 25)
    Test.assert_equals(dis(211, 50), 105.5)
    Test.assert_equals(dis(593, 61), 231.27)
    Test.assert_equals(dis(1693, 80), 338.6)
    Test.assert_equals(dis(700, 10), 630)
