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


n = 1
jump = 2
dia = 1
primes = 0
while True:
    for x in range(3):
        n += jump
        if primality(n):
            primes += 1
    n += jump
    dia += 4
    if (primes / dia) < 0.10:
        break
    jump += 2
print(jump + 1)
