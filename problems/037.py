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


def trunc(n):
    n = str(n)
    for i in range(1, len(n)):
        if not primality(int(n[i:])):
            return False
    for i in range(1, len(n)):
        if not primality(int(n[:i])):
            return False
    return True


sum = 0
for i in range(10, 1000000):
    if primality(i):
        if trunc(i):
            sum += i
print(sum)
