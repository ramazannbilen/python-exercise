"""
Harmonic Series
In mathematics, the harmonic series is the divergent infinite series:

Alternative Text

Its name derives from the concept of overtones, or harmonics in music.

Create a function that, given a precision parameter n, returns the value of the partial sum of the harmonic series up to n terms.

Examples
harmonic(3) ➞ 1.833

harmonic(1) ➞ 1.0

harmonic(5) ➞ 2.283
Notes
Round the result to the third decimal place.
"""

from edabit.Test import Test


def harmonic(n):
    summ = 0
    if n == 0:
        return 0
    else:
        for i in range(1, n + 1):
            summ += (1 / i)
    return round(summ,3)


Test.assert_equals(harmonic(10), 2.929)
Test.assert_equals(harmonic(1), 1)
Test.assert_equals(harmonic(12345), 9.998)
Test.assert_equals(harmonic(0), 0)
Test.assert_equals(harmonic(5000), 9.095)
Test.assert_equals(harmonic(2), 1.5)
