"""Stalactites or Stalagmites?
Stalactites hang from the ceiling of a cave while stalagmites grow from the floor.

Create a function that determines whether the input represents "stalactites" or "stalagmites". If it represents both, return "both". Input will be a 2D list, with 1 representing a piece of rock, and 0 representing air space.

Examples
mineral_formation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]) ➞ "stalactites"

mineral_formation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "stalagmites"

mineral_formation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "both"
Notes
There won't be any examples where both stalactites and stalagmites meet (because those are called pillars).
There won't be any example of neither stalactites or stalagmites.
In other words, if the first list has 1s, return "stalactites". If the last list has 1s, return "stalagmites". If both have them, return "both"."""


from edabit.Test import Test

def mineral_formation(cave):
    f = [i for i in cave[0] if i == 1]
    l = [i for i in cave[-1] if i == 1]
    if f and not l:
        return "stalactites"
    elif not f and l:
        return "stalagmites"
    else:
        return "both"

Test.assert_equals(mineral_formation([
[0, 1, 0, 1],
[0, 1, 0, 1],
[0, 0, 0, 1],
[0, 0, 0, 0]
]), 'stalactites')

Test.assert_equals(mineral_formation([
[0, 0, 0, 0],
[0, 1, 0, 1],
[0, 1, 1, 1],
[0, 1, 1, 1]
]), 'stalagmites')

Test.assert_equals(mineral_formation([
[1, 0, 1, 0],
[1, 1, 0, 1],
[0, 1, 1, 1],
[0, 1, 1, 1]
]), 'both')

Test.assert_equals(mineral_formation([
[1],
[1],
[0],
[0]
]), 'stalactites')

Test.assert_equals(mineral_formation([
[1],
[1],
[0],
[1]
]), 'both')

Test.assert_equals(mineral_formation([
[0],
[1],
[1],
[1]
]), 'stalagmites')

Test.assert_equals(mineral_formation([
[0, 1],
[1, 1],
[1, 1],
[1, 0]
]), 'both')

Test.assert_equals(mineral_formation([
[0, 0],
[1, 1],
]), 'stalagmites')

Test.assert_equals(mineral_formation([
[1, 1],
[0, 0],
]), 'stalactites')