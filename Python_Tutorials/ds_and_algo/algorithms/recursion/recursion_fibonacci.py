def fibonacci(n):
    assert 0 <= n == int(n), "Please enter a positive integer"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fb = fibonacci(5)
print(fb)


def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)


print(pow(2, 4))
