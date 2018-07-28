def prime_factors_2(n):
    if n < 2:
        return {}
    factors = {}
    while n % 2 == 0:
        n //= 2
        factors[2] = factors[2] + 1 if 2 in factors else 1
    while n % 3 == 0:
        n //= 3
        factors[3] = factors[3] + 1 if 3 in factors else 1
    i = 5
    limit = int(n**0.5)
    while i <= limit:
        if n % i == 0:
            n //= i
            limit = int(n**0.5)
            factors[i] = factors[i] + 1 if i in factors else 1
        elif n % (i + 2) == 0:
            n //= i + 2
            limit = int(n**0.5)
            factors[i + 2] = factors[i + 2] + 1 if i + 2 in factors else 1
        else:
            i += 6
    if n != 1:
        factors[n] = factors[n] + 1 if n in factors else 1
    return factors


def divisors(n):
    box = prime_factors_2(n)
    pro = 1
    for i in box.values():
        pro *= (i + 1)
    return pro


n = 0
while True:
    n += 1
    tri = (n**2 + n) // 2
    div = divisors(tri)
    if div > 500:
        break
print(tri)
