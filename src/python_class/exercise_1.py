# If we list all the natural numbers below 10
# that are multiples of 3 or 5, we get 3,5,6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


from typing import Callable


def cutLowX(mult: int, condition: Callable[[int], bool]) -> set[int]:
    result = {0}
    counter = 1

    while True:
        if condition(counter):  # mult * counter >= limit:
            break
        result.add(mult * counter)
        counter = counter + 1

    return result


def belowX(limit: int) -> int:
    result = cutLowX(3, lambda counter: 3 * counter >= limit)
    result.update(cutLowX(5, lambda counter: 5 * counter >= limit))

    return sum(result)
