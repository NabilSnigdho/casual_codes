"""Though these functions are already defined in math module,
it's a fun exercise to implement them."""
from math import prod


def perm(n: int, r: int) -> int:
    """permutation"""
    if n < r or r < 0:
        raise OverflowError()
    if r == 0:
        return 1
    return prod(range(n, n - r, -1))


def factorial(n: int) -> int:
    """Return x factorial as an integer."""
    return perm(n, n)


def comb(n: int, r: int) -> int:
    """Return the number of ways to choose k items
    from n items without repetition and without order."""
    if r > (n // 2):
        return comb(n, n - r)
    return perm(n, r) // factorial(r)
