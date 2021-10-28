"""List Multiplier
Create a function that takes a list as an argument and returns a new nested list for each element in the original list. The nested list must be filled with the corresponding element (string or number) in the original list and each nested list has the same amount of elements as the original list.

Examples
multiply([4, 5]) ➞ [[4, 4], [5, 5]]

multiply(["*", "%", "$"]) ➞ [["*", "*", "*"], ["%", "%", "%"], ["$", "$", "$"]]

multiply(["A", "B", "C", "D", "E"]) ➞ [["A", "A", "A", "A", "A"], ["B", "B", "B", "B", "B"], ["C", "C", "C", "C", "C"], ["D", "D", "D", "D", "D"], ["E", "E", "E", "E", "E"]]
Notes
The given list contains numbers or strings."""

from edabit.Test import Test


def multiply(l):
    ml = []
    for i in range(len(l)):
        ml.append([])
        for j in range(len(l)):
            ml[i].append(l[i])
    return ml


Test.assert_equals(multiply(["*", "%", "$"]), [["*", "*", "*"], ["%", "%", "%"], ["$", "$", "$"]])
Test.assert_equals(multiply([4, 5]), [[4, 4], [5, 5]])
Test.assert_equals(multiply(["A", "B", "C", "D", "E"]),
                   [["A", "A", "A", "A", "A"], ["B", "B", "B", "B", "B"], ["C", "C", "C", "C", "C"],
                    ["D", "D", "D", "D", "D"], ["E", "E", "E", "E", "E"]])
Test.assert_equals(multiply([1]), [[1]])
