def triple(A):
    if A % 2 != 0:
        return -1
    m = int((A / 4)**0.5)
    while True:
        m += 1
        if A % (2 * m) == 0:
            n = A // (2 * m) - m
            if n <= 0:
                return -1
            elif n < m:
                return 2 * (n * m**5 - m * n**5)


print(triple(1000))
