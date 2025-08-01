from python_class.exercise_1 import belowX, cutlowX


def test_example() -> None:
    assert 23 == belowX(10)


def test_example3() -> None:
    assert 18 == cutlowX(10, 3)


def test_example5() -> None:
    assert 5 == cutlowX(10, 5)


def test_wanted() -> None:
    assert 233168 == belowX(1_000)
