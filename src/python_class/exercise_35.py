# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below: 100: 2,3,5,7,11,13,17,31,37,71,73,79 and 97
# How many circular primes are there below one million?


# verifica se é primo
def prime(n: int) -> bool:

    if n < 2:
        return False

    if n == 2:
        return True

    for i in range(2, n - 1):

        if n % i == 0:
            return False

    return True


# faz uma rotação
def rotate(n: int) -> int:

    digits = list(str(n))
    rotated = digits[-1:] + digits[:-1]

    return int("".join(rotated))


# conta o numero de rotações necessárioas
def nbRotate(n: int) -> int:

    digits = list(str(n))

    return len(digits)


# verifica se é um primo circular
def isCircularPrime(numb: int) -> bool:

    tam = nbRotate(numb)
    if not prime(numb):
        return False

    for _ in range(1, tam):
        numb = rotate(numb)
        if not prime(numb):
            return False
    return True


# armazena os numeros circulares
def takeAllCircular(numb: int) -> set[int]:
    result = set()

    for pri in range(2, numb):
        if isCircularPrime(pri):
            result.add(pri)

    return result
