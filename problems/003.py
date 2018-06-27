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


num = 600851475143
print(primefactor(num)[-1])
