# Surprisingly there are only three numbers that can be
# written as the sum of fourth powers of their digits:
# 1634 = 1⁴+6⁴+3⁴+4⁴
# 8208 = 8⁴+2⁴+0⁴+8⁴
# 9474 = 9⁴+4⁴+7⁴+4⁴

# As 1 = 1^4  is not a sum it is not included.
# The sum of these numbers is 1634+8208+9474=19316
# Find the sum of all the numbers that
# can be written as the sum of fifth powers of their digits.


def higherLimit(power1: int) -> int:
    k = 1
    while True:
        maxSumNumb = k * (9**power1)
        minNumb = 10 ** (k - 1)
        if maxSumNumb < minNumb:
            break
        k += 1
    return int((k - 1) * (9**power1))


def powersDigits(pow: int) -> int:
    result = {0}
    limit = higherLimit(pow)
    for n in range(2, limit):
        if n == sum(int(d) ** pow for d in str(n)):
            result.add(n)
    return sum(result)
