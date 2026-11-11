# Q6 - Recursion and Its Limits

from functools import lru_cache


def ways(n):
    if n <= 1:
        return 1
    return ways(n - 1) + ways(n - 2)


@lru_cache(None)
def memo(n):
    if n <= 1:
        return 1
    return memo(n - 1) + memo(n - 2)


def iterative(n):
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


n = int(input("Enter steps: "))

print("Normal Recursion:", ways(n))
print("Memoisation:", memo(n))
print("Iteration:", iterative(n))
