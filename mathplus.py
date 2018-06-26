def expansion(power, terms, mask=None):
    if type(mask) != dict and mask is not None:
        raise TypeError("mask must be of type 'dict'")
    if mask is None:
        mask = {}
        for i in range(terms):
            mask[i + 1] = 1
    dist = dict(mask)
    for i in range(1, power):
        temp = {}
        for j in mask:
            for k in dist:
                if j + k not in temp:
                    temp[j + k] = dist[k] * mask[j]
                else:
                    temp[j + k] += dist[k] * mask[j]
        dist = dict(temp)
    return dist


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


def prime_factors(n):
    if type(n) != int:
        raise TypeError("argument must be of type 'int'")
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)
    i = 3
    limit = int(n**0.5 + 1)
    while i <= limit:
        if n % i == 0:
            n //= i
            limit = int(n**0.5 + 1)
            factors.append(i)
            continue
        i += 2
    if n != 1:
        factors.append(int(n))
    return factors


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
