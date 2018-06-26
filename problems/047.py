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


for i in range(1000000):
    if len(set(primefactor(i))) == 4:
        if len(set(primefactor(i + 1))) == 4:
            if len(set(primefactor(i + 2))) == 4:
                if len(set(primefactor(i + 3))) == 4:
                    break
print(i)
