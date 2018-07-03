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


def gold(n):
    for i in range(1, int((n / 2)**0.5) + 1):
        if primality(n - 2 * (i**2)):
            return True
    return False


i = 1
while True:
    i += 2
    if primality(i):
        continue
    elif gold(i):
        continue
    else:
        break
print(i)
