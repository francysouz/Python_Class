from python_class.exercise_35 import nbRotate, prime, rotate, isCircularPrime


def test_example() -> None:
    assert True == prime(2)


def test_example1() -> None:
    assert True == prime(197)


def test_example2() -> None:
    assert 3 == nbRotate(197)


def test_example3() -> None:
    assert 719 == rotate(197)


def test_example4() -> None:
    assert {0, 197, 719, 971} == takeAllCircular(197)


def test_example5() -> None:
    assert True == isCircularPrime(197)


def test_example6() -> None:
    assert False == isCircularPrime(8)
