def countdown(n):
    while n > 0:
        yield n
        n -= 1


generator = countdown(5)
print(next(generator))
print(next(generator))
print(next(generator))

for value in generator:
    print(value)

import sys


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


# 斐波那契数列
f = fibonacci(10)
while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        sys.exit()
