# n! means n(n-1)(n-2)...3*2*1.
#
# For example, 10! = 10*9... = 3628800,
# and the sum of the digits in the number 10! is 27
#
# Find the sum of the digits in the number 100!.
import math


def factorialMath(x: int) -> int:
    """_summary_

    Args:
        x (int): _description_

    Returns:
        int: _description_
    """
    resultado = math.factorial(x)
    return resultado


def factorialRaw(x: int) -> int:
    resultado = 1
    for i in range(2, x + 1):
        resultado *= i
    return resultado


def sumDigits(x: int) -> int:
    digits = list(str(x))
    sumDigits = 0
    for i in range(0, (len(digits))):
        sumDigits = sumDigits + int(digits[i])

    return sumDigits


def sumDigits2(x: int) -> int:
    return sum(int(d) for d in str(x))
