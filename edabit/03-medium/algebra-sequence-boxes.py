"""Algebra Sequence — Boxes
Create a function that takes a number (step) as an argument and returns the amount of boxes in that step of the sequence.

Box Sequence Image

Step 0: Start with 0
Step 1: Add 3
Step 2: Subtract 1
Repeat Step 1 & 2 ...
Examples
box_seq(0) ➞ 0

box_seq(1) ➞ 3

box_seq(2) ➞ 2
Notes
Step (the input) is always a positive integer (or zero)."""

from edabit.Test import Test


def box_seq(step):
    boxes = 0
    for i in range(1, step + 1):
        if i % 2 == 1:
            boxes += 3
        else:
            boxes -= 1
    return boxes


Test.assert_equals(box_seq(5), 7)
Test.assert_equals(box_seq(0), 0)
Test.assert_equals(box_seq(6), 6)
Test.assert_equals(box_seq(99), 101)
Test.assert_equals(box_seq(2), 2)
Test.assert_equals(box_seq(1), 3)
