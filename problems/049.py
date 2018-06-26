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


def group(n):
    n = str(n)
    box = []
    for x in n:
        box.append(x)
    box.sort()
    return box


flag = False
for i in range(1000, 10000):
    if primality(i):
        for j in range(i + 1, (10000 // 2) + (i // 2)):
            if primality(j):
                if group(i) == group(j):
                    k = 2 * j - i
                    if primality(k):
                        if group(i) == group(k):
                            print(i, j, k)
