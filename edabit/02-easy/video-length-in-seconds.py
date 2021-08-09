"""
Video Length in Seconds
You are given the length of a video in minutes. The format is mm:ss (e.g.: "02:54"). Create a function that takes the video length and return it in seconds.

Examples
minutes_to_seconds("01:00") ➞ 60

minutes_to_seconds("13:56") ➞ 836

minutes_to_seconds("10:60") ➞ False
Notes
The video length is given as a string.
If the number of seconds is 60 or over, return False (see example #3).
You may get a number of minutes over 99 (e.g. "121:49" is perfectly valid).
"""

from edabit.Test import Test


def minutes_to_seconds(time):
    t2 = time.split(":")
    m = int(t2[0]) * 60
    s = int(t2[1])
    if int(t2[1]) >= 60:
        return False
    else:
        return m + s


if __name__ == '__main__':
    Test.assert_equals(minutes_to_seconds("01:00"), 60)
    Test.assert_equals(minutes_to_seconds("13:56"), 836)
    Test.assert_equals(minutes_to_seconds("10:60"), False)
    Test.assert_equals(minutes_to_seconds("132:21"), 7941)
    Test.assert_equals(minutes_to_seconds("132:271"), False)
    Test.assert_equals(minutes_to_seconds("01:30"), 90)
    Test.assert_equals(minutes_to_seconds("10:00"), 600)
