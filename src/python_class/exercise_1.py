# If we list all the natural numbers below 10
# that are multiples of 3 or 5, we get 3,5,6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


def cutlowX(limit: int, mult: int) -> int:
    result = [0]
    counter = 1
    while True:
        if mult * counter >= limit:
            break
        result.append(mult * counter)
        counter = counter + 1
    return sum(result)


def belowX(limit: int) -> int:
    resul3 = cutlowX(limit, 3)
    resul5 = cutlowX(limit, 5)

    return resul3 + resul5
