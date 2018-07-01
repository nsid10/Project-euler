def primality(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5 + 1), 2):
        if n % i == 0:
            return False
    return True


def prime_sieve(n):
    if n < 3:
        return []
    numbers = [True] * (n // 2)
    for i in range(3, int(n**0.5 + 1), 2):
        if numbers[(i - 1) // 2]:
            for j in range(i * i, n, 2 * i):
                numbers[(j - 1) // 2] = False
    sieve = [2]
    for i in range(1, n // 2):
        if numbers[i]:
            sieve.append(2 * i + 1)
    return sieve


sieve = prime_sieve(1000)
long = 0
for b in sieve:
    for a in range(-b, 0, 2):
        n = 0
        while primality(n**2 + a * n + b):
            n += 1
        if long < n:
            long = n
            long_a = a
            long_b = b
print(long_a * long_b)
