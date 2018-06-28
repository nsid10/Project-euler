def prime_sieve(n):
    if n < 3:
        return []
    numbers = [True] * (n // 2)
    for i in range(3, int(n**0.5 + 1), 2):
        if numbers[(i - 1) // 2]:
            for j in range(i * i, n, 2 * i):
                numbers[(j - 1) // 2] = False
    sieve = {2: 2}
    last = 2
    for i in range(1, n // 2):
        if numbers[i]:
            sieve[2 * i + 1] = 2 * i + 1 + last
            last = sieve[2 * i + 1]
    return sieve


sieve = prime_sieve(1000000)

t = int(input().strip())
for x in range(t):
    n = int(input().strip())
    while n not in sieve:
        n -= 1
    print(sieve[n])
