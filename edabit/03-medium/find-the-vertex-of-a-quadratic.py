"""Find the Vertex of a Quadratic
Every quadratic curve y = a x² + b x + c has a vertex point: the turning point where the curve stops heading down and starts going up.

Given the values a, b and c, you need to return the coordinates of the vertex. Return your answers rounded to 2 decimal places.

Examples
find_vertex(1, 0, 25)  ➞ [0, 25]
# The vertex of y=x²+25 is at (0, 25).

find_vertex(-1, 0, 25) ➞ [0, 25]
# The vertex of y=-x²+25 is at (0, 25).

find_vertex(1, 10, 4) ➞ [-5, -21]
# The vertex of y=x²+10x+4 is at (-5, -21).
Notes
See Resources if you're not sure how to find the x or y coordinates of the vertex.
a will always be non-zero."""

from edabit.Test import Test


def find_vertex(a, b, c):
    x_coor = -1 * (b / (2 * a))
    y_coor = a * ((x_coor) ** 2) + b * x_coor + c
    return [x_coor, y_coor]


Test.assert_equals(find_vertex(-1, 0, 25), [0, 25])
Test.assert_equals(find_vertex(1, 10, 25), [-5, 0])
Test.assert_equals(find_vertex(8, 4, 0), [-0.25, -0.5])
Test.assert_equals(find_vertex(4, -200, 1000), [25, -1500])
Test.assert_equals(find_vertex(1, -50, -1000), [25, -1625])
Test.assert_equals(find_vertex(-1, 20, 600), [10, 700])
Test.assert_equals(find_vertex(5, 1, 20), [-0.1, 19.95])
