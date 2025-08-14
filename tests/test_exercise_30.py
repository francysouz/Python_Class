from python_class.exercise_30 import (
    powersDigits,
    higherLimit,
)


def test_example() -> None:
    assert 354294 == higherLimit(5)


def test_example2() -> None:
    assert 19316 == powersDigits(4)


def test_example3() -> None:
    assert 443839 == powersDigits(5)
