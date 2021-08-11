"""
Distance Between Two Points
In this challenge, you have to find the distance between two points placed on a Cartesian plane. Knowing the coordinates of both the points, you have to apply the Pythagorean theorem to find the distance between them.

Two points on a Cartesian plane

Given two dictionaries a and b being the two points coordinates (x and y), implement a function that returns the distance between the points, rounded to the nearest thousandth.

Examples
get_distance({"x": -2, "y": 1}, {"x": 4, "y": 3}) ➞ 6.325

get_distance({"x": 0, "y": 0}, {"x": 1, "y": 1}) ➞ 1.414

get_distance({"x": 10, "y": -5}, {"x": 8, "y": 16}) ➞ 21.095
Notes
Take a look at the Resources tab if you need a refresher on the geometry related to this challenge.
The "distance" is the shortest distance between the two points, or the straight line generated from a to b.
"""

from edabit.Test import Test


def get_distance(a, b):
    xaxis = [a['x'], b['x']] #pythagorean
    yaxis = [a['y'], b['y']]
    xlong = abs(xaxis[0] - xaxis[1])
    ylong = abs(yaxis[0] - yaxis[1])
    return  round((xlong**2 + ylong**2)**(1/2),3)

if __name__ == '__main__':
    Test.assert_equals(get_distance({"x": -2, "y": 1}, {"x": 4, "y": 3}), 6.325)
    Test.assert_equals(get_distance({"x": 0, "y": 0}, {"x": 1, "y": 1}), 1.414)
    Test.assert_equals(get_distance({"x": 10, "y": -5}, {"x": 8, "y": 16}), 21.095)
    Test.assert_equals(get_distance({"x": 4, "y": 3}, {"x": 3, "y": -2}), 5.099)
    Test.assert_equals(get_distance({"x": -1, "y": -1}, {"x": 10, "y": 10}), 15.556)
    Test.assert_equals(get_distance({"x": 100, "y": 100}, {"x": 100, "y": 100}), 0)
    Test.assert_equals(get_distance({"x": 14239, "y": -11222}, {"x": -12301, "y": 12888}), 35856.153)
