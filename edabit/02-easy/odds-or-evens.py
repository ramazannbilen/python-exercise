"""
Odds vs. Evens
Given an integer, return "odd" if the sum of all odd digits is greater than the sum of all even digits. Return "even" if the sum of even digits is greater than the sum of odd digits, and "equal" if both sums are the same.

Examples
odds_vs_evens(97428) ➞ "odd"
# odd = 16 (9+7)
# even = 14 (4+2+8)

odds_vs_evens(81961) ➞ "even"
# odd = 11 (1+9+1)
# even = 14 (8+6)

odds_vs_evens(54870) ➞ "equal"
# odd = 12 (5+7)
# even = 12 (4+8+0)
Notes
N/A
"""

from edabit.Test import Test


def odds_vs_evens(num):
    nums = str(num)
    odds = [int(i) for i in nums if int(i) % 2 != 0]
    evens = [int(i) for i in nums if int(i) % 2 == 0]
    if sum(odds) > sum(evens):
        return "odd"
    elif sum(odds) < sum(evens):
        return "even"
    else:
        return "equal"


if __name__ == '__main__':
    Test.assert_equals(odds_vs_evens(44547), 'equal')
    Test.assert_equals(odds_vs_evens(412420), 'even')
    Test.assert_equals(odds_vs_evens(128797), 'odd')
    Test.assert_equals(odds_vs_evens(838768), 'even')
    Test.assert_equals(odds_vs_evens(371910), 'odd')
    Test.assert_equals(odds_vs_evens(769431), 'odd')
    Test.assert_equals(odds_vs_evens(221294), 'equal')
    Test.assert_equals(odds_vs_evens(859307), 'odd')
    Test.assert_equals(odds_vs_evens(847617), 'even')
    Test.assert_equals(odds_vs_evens(348466), 'even')
    Test.assert_equals(odds_vs_evens(50236), 'equal')
    Test.assert_equals(odds_vs_evens(133987), 'odd')
    Test.assert_equals(odds_vs_evens(698570), 'odd')
    Test.assert_equals(odds_vs_evens(822406), 'even')
    Test.assert_equals(odds_vs_evens(54313), 'odd')
    Test.assert_equals(odds_vs_evens(17788), 'even')
    Test.assert_equals(odds_vs_evens(72083), 'equal')
    Test.assert_equals(odds_vs_evens(649924), 'odd')
    Test.assert_equals(odds_vs_evens(968740), 'even')
    Test.assert_equals(odds_vs_evens(942674), 'equal')
