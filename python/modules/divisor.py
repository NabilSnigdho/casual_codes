from math import isqrt, prod
from functools import cache


@cache
def divisors(num: int) -> list[int]:
    """List all the divisors of a positive integers"""
    if num <= 0:
        raise ValueError("Only positive integers allowed!")
    if num == 1:
        return [1]
    l, r = [1], [num]
    for i in range(2, root := isqrt(num - 1) + 1):
        if num % i == 0:
            l.append(i)
            r.insert(0, num // i)
    if root**2 == num:
        l.append(root)
    return l + r


def tau(num: int) -> int:
    """divisor tau function"""
    return len(divisors(num))


def sigma_1(num: int) -> int:
    """divisor sigma_1 function"""
    return sum(divisors(num))


def product(num: int) -> int:
    """divisor product function"""
    return prod(divisors(num))
