"""Basic Arithmetic Operations on a String Number
Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

For example:

"15 // 0"  ➞ -1
Examples
arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24

arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0

arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144

arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1
Notes
All the inputs are only integers.
The operators are * - + and //.
Hint: Think about the single space that appears before and after the arithmetic operator."""

from edabit.Test import Test

def arithmetic_operation(n):
    a = n.split(" ")
    if a[1] == "+":
        return int(a[0]) + int(a[-1])
    elif a[1] == "-":
        return int(a[0]) - int(a[-1])
    elif a[1] == "*":
        return int(a[0]) * int(a[-1])
    else:
        if a[2] == 0:
            return -1
        else:
            return int(a[0]) / int(a[-1])

Test.assert_equals(arithmetic_operation("12 + 12"), 24)
Test.assert_equals(arithmetic_operation("22 - 12"), 10)
Test.assert_equals(arithmetic_operation("100 * 12"), 1200)
Test.assert_equals(arithmetic_operation("120 // 10"), 12)
Test.assert_equals(arithmetic_operation("122 // 0"), -1)
Test.assert_equals(arithmetic_operation("10 * 20"), 200)
Test.assert_equals(arithmetic_operation("10 - 10"), 0)
Test.assert_equals(arithmetic_operation("10 - 12"), -2)