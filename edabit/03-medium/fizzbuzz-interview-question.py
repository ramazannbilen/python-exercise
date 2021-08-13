"""

"""

from edabit.Test import Test

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 != 0:
        return "Fizz"
    elif num % 5 == 0 and num % 3 != 0:
        return "Buzz"
    elif num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    else:
        return str(num)


if __name__ == '__main__':
    Test.assert_equals(fizz_buzz(3), "Fizz")
    Test.assert_equals(fizz_buzz(5), "Buzz")
    Test.assert_equals(fizz_buzz(15), "FizzBuzz")
    Test.assert_equals(fizz_buzz(10), "Buzz")
    Test.assert_equals(fizz_buzz(98), "98")