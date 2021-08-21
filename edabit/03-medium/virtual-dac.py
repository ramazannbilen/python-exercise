"""
Virtual DAC
In electronics, a digital-to-analog converter (DAC, D/A, or D-to-A) is a system that
converts a binary representation of that signal into an analog output.
An 8 bit converter can represent a maximum of 2^8 different values,
with each successive value differing by 1/256 of the full scale value,
this becomes the system resolution.

Create a function that takes a decimal number representation of a signal and
returns the analog voltage level that would be created by a DAC
if it were given the same number in binary.

While value range is 0-1023, reference range is 0-5.00 volts.
Value and reference is directly proportional.

This DAC has 10 bits of resolution and the DAC reference is set at 5.00 volts.

Examples
V_DAC(0) ➞ 0

V_DAC(1023) ➞ 5

V_DAC(400) ➞ 1.96
Notes
You should return your value rounded to two decimal places.
"""

from edabit.Test import Test


def V_DAC(value):
    return round((value / 1023) * 5, 2)


if __name__ == '__main__':
    Test.assert_equals(V_DAC(1023), 5)
    Test.assert_equals(V_DAC(0), 0)
    Test.assert_equals(V_DAC(500), 2.44)
    Test.assert_equals(V_DAC(400), 1.96)
    Test.assert_equals(V_DAC(850), 4.15)
