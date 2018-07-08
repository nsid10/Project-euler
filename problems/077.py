def prime_sieve(n):
    if type(n) != int:
        raise TypeError("argument must be of type 'int'")
    if n < 3:
        return []
    number = [False] + [True] * (n // 2 - 1)
    for i in range(3, int(n**0.5 + 1), 2):
        if number[(i - 1) // 2]:
            number[i**2 // 2::i] = [False] * ((n - 1) // i - (n - 1) // (2 * i) - (i - 1) // 2)
    return [2] + [2 * i + 1 for i in range(n // 2) if number[i]]


sieve = prime_sieve(100)
target = 0
while True:
    target += 1
    ways = [1] + [0] * target
    for i in range(len(sieve)):
        for j in range(sieve[i], target + 1):
            ways[j] += ways[j - sieve[i]]
    if ways[-1] > 5000:
        break
print(target)
