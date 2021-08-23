"""Cricket Balls to Overs!
In cricket, an over consists of six deliveries a bowler bowls from one end. Create a function that takes the number of balls bowled by a bowler and calculates the number of overs and balls bowled by him/her. Return the value as a float, in the format overs.balls.

Examples
total_overs(2400) ➞ 400

total_overs(164) ➞ 27.2
# 27 overs and 2 balls were bowled by the bowler.

total_overs(945) ➞ 157.3
# 157 overs and 3 balls were bowled by the bowler.

total_overs(5) ➞ 0.5
Notes
The number following the decimal point represents the balls remaining after the last over. Therefore, it will only ever have a value of 1-5.
"""

from edabit.Test import Test


def total_overs(balls):
    m = balls // 6
    n = balls % 6
    return float(m + 0.1 * n)


Test.assert_equals(total_overs(2400), 400)
Test.assert_equals(total_overs(164), 27.2)
Test.assert_equals(total_overs(945), 157.3)
Test.assert_equals(total_overs(5), 0.5)
Test.assert_equals(total_overs(7), 1.1)
Test.assert_equals(total_overs(15), 2.3)
Test.assert_equals(total_overs(0), 0)
