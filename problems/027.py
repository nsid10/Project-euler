def primality(n):
    if type(n) != int:
        raise TypeError("argument must be of type 'int'")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    return True


def quad(a, b):
    n = 0
    while True:
        if not primality(n**2 + a * n + b):
            break
        n += 1
    return n


long = 0
for a in range(-999, 1001, 2):
    if not primality(abs(a)):
        continue
    for b in range(1001):
        if a + b <= 0 or abs(a) > b:
            continue
        if primality(b):
            if quad(a, b) > long:
                long = quad(a, b)
                long_a = a
                long_b = b
print(long)
print(long_a * long_b)
