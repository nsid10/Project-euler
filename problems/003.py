def primefactor(n):
    if type(n) != int:
        raise TypeError("argument must be of type 'int'")
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    x = 3
    limit = int(n**0.5 + 1)
    while x <= limit:
        if n % x == 0:
            n /= x
            limit = int(n**0.5 + 1)
            factors.append(x)
            continue
        x += 2
    if n != 1:
        factors.append(int(n))
    return factors


num = 600851475143
print(primefactor(num)[-1])
