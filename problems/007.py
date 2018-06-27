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


print(prime_sieve(125000)[10001 - 1])
