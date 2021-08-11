"""
Get Sum of People's Budget
Create the function that takes a list of dictionaries and returns the sum of people's budgets.

Examples
get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]) ➞ 65700

get_budgets([
  { "name": "John",  "age": 21, "budget": 29000 },
  { "name": "Steve",  "age": 32, "budget": 32000 },
  { "name": "Martin",  "age": 16, "budget": 1600 }
]) ➞ 62600
Notes
N/A
"""

from edabit.Test import Test


def get_budgets(lst):
    return sum([i["budget"] for i in lst])


if __name__ == '__main__':
    Test.assert_equals(get_budgets(
        [{"name": "John", "age": 21, "budget": 23000}, {"name": "Steve", "age": 32, "budget": 40000},
         {"name": "Martin", "age": 16, "budget": 2700}]), 65700)
    Test.assert_equals(get_budgets(
        [{"name": "John", "age": 21, "budget": 29000}, {"name": "Steve", "age": 32, "budget": 32000},
         {"name": "Martin", "age": 16, "budget": 1600}]), 62600)
    Test.assert_equals(get_budgets(
        [{"name": "John", "age": 21, "budget": 19401}, {"name": "Steve", "age": 32, "budget": 12321},
         {"name": "Martin", "age": 16, "budget": 1204}]), 32926)
    Test.assert_equals(get_budgets(
        [{"name": "John", "age": 21, "budget": 10234}, {"name": "Steve", "age": 32, "budget": 21754},
         {"name": "Martin", "age": 16, "budget": 4935}]), 36923)
