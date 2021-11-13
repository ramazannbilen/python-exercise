"""The Snake — Area Filling
This challenge is based on the classic videogame "Snake".

Assume the game screen is an n * n square, and the snake starts the game with length 1 (i.e. just the head) positioned on the top left corner.

For example, if n = 7 the game looks something like this:



In this version of the game, the length of the snake doubles each time it eats food (e.g. if the length is 4, after eating it becomes 8).

Create a function that takes the side n of the game screen and returns the number of times the snake can eat before it runs out of space in the game screen.

Examples
snakefill(3) ➞ 3

snakefill(6) ➞ 5

snakefill(24) ➞ 9
Notes
The given number will always be a positive integer (there are no exceptions to handle)."""

from edabit.Test import Test


def snakefill(n):
    size = 1
    area = n * n
    eating = 0
    while size < area:
        if area - size >= size:
            eating += 1
            size *= 2
        else:
            break

    return eating


Test.assert_equals(snakefill(8), 6)
Test.assert_equals(snakefill(18), 8)
Test.assert_equals(snakefill(555), 18)
Test.assert_equals(snakefill(2), 2)
Test.assert_equals(snakefill(1), 0)
Test.assert_equals(snakefill(900), 19)
