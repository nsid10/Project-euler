def primality(n):
    if type(n) != int:
        raise TypeError("argument must be of type 'int'")
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5 + 1), 2):
        if n % i == 0:
            return False
    return True


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


def trunc(n):
    if n < 10:
        return False
    n = str(n)
    for i in range(1, len(n)):
        if not primality(int(n[i:])):
            return False
    for i in range(1, len(n)):
        if not primality(int(n[:i])):
            return False
    return True


N = int(input())
sum = 0
for i in prime_sieve(N):
    if trunc(i):
        sum += i
print(sum)
