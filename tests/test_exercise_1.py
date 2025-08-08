from python_class.exercise_1 import belowX


def test_example() -> None:
    assert 23 == belowX(10)


def test_wanted() -> None:
    assert 233_168 == belowX(1_000)
