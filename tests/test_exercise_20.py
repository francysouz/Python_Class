from python_class.exercise_20 import factorialRaw, sumDigits, sumDigits2


def test_example() -> None:
    assert 3628800 == factorialRaw(10)


def test_example2() -> None:
    assert 5 == sumDigits(41)


def test_example3() -> None:
    assert 27 == sumDigits(factorialRaw(10))


def test_example4() -> None:
    assert 648 == sumDigits(factorialRaw(100))


def test_example5() -> None:
    assert 648 == sumDigits2(factorialRaw(100))
