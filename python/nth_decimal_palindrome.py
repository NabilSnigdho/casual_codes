from math import log10, floor


def nth_decimal_palindrome(num: int) -> int:
    """https://oeis.org/A002113"""

    if num == 0:
        return 0

    p = 10 ** floor(log10(num) - 1)
    if num > (11 * p - 2):
        p *= 10
    p = int(p)

    m = num - p + 1
    s = str(m)
    return int(s + s[-1 if m < p else -2 :: -1])


for i in range(111):
    print(nth_decimal_palindrome(i), end=" ")
