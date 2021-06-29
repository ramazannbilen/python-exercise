"""
Burglary Series (10): Calculate Difference
The insurance guy calls again and apologizes. They found another policy made by your spouse, but this one is limited to cover a particular maximum in losses (for example, 50,000€). You send a bill to your spouse for the difference you lost.

Given an dict of the stolen items and a limit, return the difference between the total value of those items and the limit of the policy.

Examples
calc_diff({ "baseball bat": 20 }, 5) ➞ 15

calc_diff({"skate": 10, "painting": 20 }, 19) ➞ 11

calc_diff({"skate": 200, "painting": 200, "shoes": 1 }, 400) ➞ 1
Notes
The dict data always contains at least an item (no empty objects).
The sum of the items is always greater than the limit.
"""

from edabit.Test import Test


def calc_diff(obj, limit):
    return sum(obj.values()) - limit        # it started to be little bit specific at built-in-functions


if __name__ == '__main__':
    from random import seed
    from random import randint

    seed(1)
    r = randint(1e3, 3e4)

    obj1 = {"skate": 20000, "painting": 30000, "shoes": 1}
    obj2 = {"baseball bat": 31}
    obj3 = {"stereo": 1110, "pillow": r}

    exp, act, anx = [1, 21, r + 10], [obj1, obj2, obj3], [5e4, 10, 11e2]
    for i, x in enumerate(exp): Test.assert_equals(x, calc_diff(act[i], anx[i]))
