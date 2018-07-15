def prime_sieve(n):
    if type(n) != int:
        raise TypeError("argument must be of type 'int'")
    if n < 3:
        return []
    number = [True] * (n // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if number[i // 2]:
            number[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if number[i]]


n = 50000000
sieve_a = prime_sieve(round(pow(n, 1 / 2)) + 1)
sieve_b = prime_sieve(round(pow(n, 1 / 3)) + 1)
sieve_c = prime_sieve(round(pow(n, 1 / 4)) + 1)

bag = set()
for c in sieve_c:
    for b in sieve_b:
        for a in sieve_a:
            triplet = a * a + b * b * b + c * c * c * c
            if triplet > n:
                break
            bag.add(triplet)

print(len(bag))
