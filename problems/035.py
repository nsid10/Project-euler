from collections import deque


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


count = 0
N = 1000000
for i in prime_sieve(N):
    word = str(i)
    d = deque(list(word))
    flag = True
    for j in range(len(word)):
        d.rotate(1)
        if not primality(int(''.join(d))):
            flag = False
            break
    if flag:
        count += 1
print(count)
