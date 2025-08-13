from python_class.exercise_35 import (
    isCircularPrime,
    nbRotate,
    prime,
    rotate,
    takeAllCircular,
)


def test_example() -> None:
    assert prime(2)


def test_example1() -> None:
    assert prime(197)


def test_example2() -> None:
    assert 3 == nbRotate(197)


def test_example3() -> None:
    assert 719 == rotate(197)


def test_example4() -> None:
    assert 13 == takeAllCircular(100)


def test_example5() -> None:
    assert isCircularPrime(197)


def test_example6() -> None:
    assert not isCircularPrime(8)


def test_example7() -> None:
    assert 55 == takeAllCircular(1_000_000)
