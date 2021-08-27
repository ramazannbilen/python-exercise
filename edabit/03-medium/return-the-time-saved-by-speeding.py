"""Return the Time Saved by Speeding
One cause for speeding is the desire to shorten the time spent traveling. In long distance trips, speeding does save an appreciable amount of time. However, the same cannot be said about short distance trips.

Create a function that calculates the amount of time saved were you traveling with an average speed that is above the speed-limit as compared to traveling with an average speed exactly at the speed-limit.

Examples
# The parameter's format is as follows:
# (speed limit, avg speed, distance traveled at avg speed)

time_saved(80, 90, 40) ➞ 3.3

time_saved(80, 90, 4000) ➞ 333.3

time_saved(80, 100, 40 ) ➞ 6.0

time_saved(80, 100, 10) ➞ 1.5
Notes
Speed = distance/time
The time returned should be in minutes, not hours.
Round the answer to one decimal place.
The speed limit and average speed are both given in mi/hr"""

from edabit.Test import Test


def time_saved(s_lim, s_avg, d):
    fmin = d / (s_lim / 60)
    lmin = d / (s_avg / 60)
    return round(fmin - lmin, 1)


Test.assert_equals(time_saved(80, 90, 40), 3.3)
Test.assert_equals(time_saved(80, 90, 4000), 333.3)
Test.assert_equals(time_saved(80, 100, 40), 6.0)
Test.assert_equals(time_saved(80, 100, 10), 1.5)
Test.assert_equals(time_saved(60, 65, 25), 1.9)
Test.assert_equals(time_saved(60, 60, 20), 0)
Test.assert_equals(time_saved(80, 95, 200), 23.7)
Test.assert_equals(time_saved(70, 92, 50), 10.2)
Test.assert_equals(time_saved(70, 92, 20), 4.1)
Test.assert_equals(time_saved(70, 100, 12), 3.1)
