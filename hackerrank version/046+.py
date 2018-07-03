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
    count = 0
    for i in range(1, int((n / 2)**0.5) + 1):
        if primality(n - 2 * (i**2)):
            count += 1
    return count


t = int(input())
for x in range(t):
    n = int(input())
    print(gold(n))
