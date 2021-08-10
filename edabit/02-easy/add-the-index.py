"""
Add the Index
Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...

Examples
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]

add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]

add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
Notes
You'll only get numbers in the list.
"""

from edabit.Test import Test


def add_indexes(lst):
    a = [i for i in enumerate(lst)]
    index = []
    for i in a:
        index.append(i[0])
    new = []
    for i in range(len(lst)):
        new.append(lst[i] + index[i])
    return new


if __name__ == '__main__':
    Test.assert_equals(add_indexes([0, 0, 0, 0, 0]), [0, 1, 2, 3, 4])
    Test.assert_equals(add_indexes([1, 2, 3, 4, 5]), [1, 3, 5, 7, 9])
    Test.assert_equals(add_indexes([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])
    Test.assert_equals(add_indexes([-25, -15, 3]), [-25, -14, 5])
    Test.assert_equals(add_indexes([27]), [27])
    Test.assert_equals(add_indexes([-48, -20, 41, 29, -25, -17, -13, 5, 4, -5, 3, -17, 23]),
                       [-48, -19, 43, 32, -21, -12, -7, 12, 12, 4, 13, -6, 35])
    Test.assert_equals(add_indexes([-32, -24, -50, 48, 5, -27, -33, -3, 16, -16, -31, -11, 43]),
                       [-32, -23, -48, 51, 9, -22, -27, 4, 24, -7, -21, 0, 55])
    Test.assert_equals(add_indexes([38, -8, 40, -50, -26, -3, -29, -33, 13, 28]),
                       [38, -7, 42, -47, -22, 2, -23, -26, 21, 37])
    Test.assert_equals(add_indexes([-1, -3, -20, 13, 19, -12, 15, 8, -49, 27, -21, 17, 41, 17, 5, -45, -33]),
                       [-1, -2, -18, 16, 23, -7, 21, 15, -41, 36, -11, 28, 53, 30, 19, -30, -17])
    Test.assert_equals(
        add_indexes([35, -48, -17, 25, 25, -45, -49, -32, -40, 48, 20, -27, -22, -1, -20, -5, 29, 18, -28, -36]),
        [35, -47, -15, 28, 29, -40, -43, -25, -32, 57, 30, -16, -10, 12, -6, 10, 45, 35, -10, -17])
    Test.assert_equals(add_indexes([-48]), [-48])
    Test.assert_equals(add_indexes([-15, -20, -28, -41, -2, -36, -18, -23, 44, -17, -12, -33, 7, 34, 5, -16]),
                       [-15, -19, -26, -38, 2, -31, -12, -16, 52, -8, -2, -22, 19, 47, 19, -1])
    Test.assert_equals(add_indexes([-20, 25, 49, -4, -20, -26, 23, 23, -50, 44, -48, -27]),
                       [-20, 26, 51, -1, -16, -21, 29, 30, -42, 53, -38, -16])
    Test.assert_equals(add_indexes([-9, 46, -17, 26, 0, -26, 12, -15, -30, -44, 29, 45, -38, -43]),
                       [-9, 47, -15, 29, 4, -21, 18, -8, -22, -35, 39, 56, -26, -30])
    Test.assert_equals(add_indexes([-44, -42, 26, -50, -29, -32, -22, 27, -31, 21, -12, -18, -13, -24, 24, 35]),
                       [-44, -41, 28, -47, -25, -27, -16, 34, -23, 30, -2, -7, -1, -11, 38, 50])
    Test.assert_equals(add_indexes([49, -28, -30, 35]), [49, -27, -28, 38])
    Test.assert_equals(add_indexes([20, -5, 25, -36, -12, 13, -30, 26, 34]), [20, -4, 27, -33, -8, 18, -24, 33, 42])
    Test.assert_equals(add_indexes([-41, -22, -41, -12]), [-41, -21, -39, -9])
    Test.assert_equals(add_indexes([-23, 26, 22]), [-23, 27, 24])
    Test.assert_equals(add_indexes([-5, 25, 19, 31, -39, 26, 4, 10, -43, -4, 26, -34, -1, -13, -26, -45]),
                       [-5, 26, 21, 34, -35, 31, 10, 17, -35, 5, 36, -23, 11, 0, -12, -30])
    Test.assert_equals(add_indexes([48, -6, 13, 39]), [48, -5, 15, 42])
    Test.assert_equals(add_indexes([18, 27, -27, -35, -19, -5, -37, 20]), [18, 28, -25, -32, -15, 0, -31, 27])
    Test.assert_equals(add_indexes([-26, 37, -29, -35, 18, 20, -25]), [-26, 38, -27, -32, 22, 25, -19])
    Test.assert_equals(add_indexes([-49, 33, -7, -25]), [-49, 34, -5, -22])
    Test.assert_equals(add_indexes([8, -21, -1, -46, 2, 48, -14, 45, 7, 12, 9, 45, -12, -8]),
                       [8, -20, 1, -43, 6, 53, -8, 52, 15, 21, 19, 56, 0, 5])
    Test.assert_equals(add_indexes([1, -12, 17, 12]), [1, -11, 19, 15])
    Test.assert_equals(add_indexes([49, 9, 11, -18, -15, -23, 32, 44, 33]), [49, 10, 13, -15, -11, -18, 38, 51, 41])
    Test.assert_equals(add_indexes([22, -50, 36, 12, 2, -48, 2, -21, -49, -47]),
                       [22, -49, 38, 15, 6, -43, 8, -14, -41, -38])
    Test.assert_equals(add_indexes([-44, 6, 16, -35, -30]), [-44, 7, 18, -32, -26])
    Test.assert_equals(add_indexes([40, -38, -17, 24, -41, 43, -34, 11, -38, -42, -1, 16, 20]),
                       [40, -37, -15, 27, -37, 48, -28, 18, -30, -33, 9, 27, 32])
    Test.assert_equals(add_indexes([-31, -5, -5]), [-31, -4, -3])
    Test.assert_equals(add_indexes([-44, 11, 26, 40, 3, 50, 3, 42, -1, 40, -12, 48, 0, 18, 1, -28, -18, 47, 45, 2]),
                       [-44, 12, 28, 43, 7, 55, 9, 49, 7, 49, -2, 59, 12, 31, 15, -13, -2, 64, 63, 21])
    Test.assert_equals(add_indexes([21, -10, -49]), [21, -9, -47])
    Test.assert_equals(add_indexes([-45, 49, 6, -50, 12, -30, 36, -36, -3, -28, 7, -47, -24, 34, 39, 45, 25]),
                       [-45, 50, 8, -47, 16, -25, 42, -29, 5, -19, 17, -36, -12, 47, 53, 60, 41])
    Test.assert_equals(add_indexes([-4, 45]), [-4, 46])
    Test.assert_equals(add_indexes([42, -48, 40, -40, -17, -35, -16, 46]), [42, -47, 42, -37, -13, -30, -10, 53])
    Test.assert_equals(add_indexes([-28]), [-28])
    Test.assert_equals(add_indexes([-6, 12, -39, 40, 23, 33, -44]), [-6, 13, -37, 43, 27, 38, -38])
    Test.assert_equals(add_indexes([-14, 10, 21, 40, 35, -36]), [-14, 11, 23, 43, 39, -31])
    Test.assert_equals(add_indexes([-33, -35, 34, -39, -18, 17, -44, -23, -30, 43]),
                       [-33, -34, 36, -36, -14, 22, -38, -16, -22, 52])
    Test.assert_equals(add_indexes([-45, -22, 18, 26, -37, -26, 26, 37, -7, -31]),
                       [-45, -21, 20, 29, -33, -21, 32, 44, 1, -22])
    Test.assert_equals(add_indexes([-32, 41, -14, -43, 30, -24, -30, -18, 21, 30, 39, -45, -11, 9, 5, -12, -3]),
                       [-32, 42, -12, -40, 34, -19, -24, -11, 29, 39, 49, -34, 1, 22, 19, 3, 13])
    Test.assert_equals(add_indexes([-9, 21, 17, 48, -36, -16, 24, -15, -41, 47, -28, 2, 28, -12, 40, 27]),
                       [-9, 22, 19, 51, -32, -11, 30, -8, -33, 56, -18, 13, 40, 1, 54, 42])
    Test.assert_equals(add_indexes([4, 1, 16, -45, 47, -38, -18]), [4, 2, 18, -42, 51, -33, -12])
    Test.assert_equals(add_indexes([12, 36, -42, 38]), [12, 37, -40, 41])
    Test.assert_equals(add_indexes([-19, 12, 19, 39]), [-19, 13, 21, 42])
    Test.assert_equals(add_indexes([5, -4, 26, 1, -43, 17, 14, -44, -40, 22, -22, -32, -13, -21, 50, 4, 12]),
                       [5, -3, 28, 4, -39, 22, 20, -37, -32, 31, -12, -21, -1, -8, 64, 19, 28])
    Test.assert_equals(add_indexes([-13, -33]), [-13, -32])
    Test.assert_equals(add_indexes([-27, 46, 24, 36, 13, -18, 12]), [-27, 47, 26, 39, 17, -13, 18])
    Test.assert_equals(add_indexes([-42, 18]), [-42, 19])
    Test.assert_equals(
        add_indexes([-5, -10, -6, -34, 32, 15, 9, 32, 20, 36, -16, 5, -42, 14, -35, 22, -18, -29, -17, 29]),
        [-5, -9, -4, -31, 36, 20, 15, 39, 28, 45, -6, 16, -30, 27, -21, 37, -2, -12, 1, 48])
    Test.assert_equals(add_indexes([42, -33, 29, -14, 45, -43, 4, 2, 8, -45, 46, 38, 16]),
                       [42, -32, 31, -11, 49, -38, 10, 9, 16, -36, 56, 49, 28])
    Test.assert_equals(add_indexes([-14, 28]), [-14, 29])
