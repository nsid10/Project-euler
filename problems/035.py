from collections import deque


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


count = 0
for i in range(1000000):
    if primality(i):
        word = str(i)
        d = deque(list(word))
        flag = True
        for j in range(len(word)):
            d.rotate(1)
            if not primality(int(''.join(d))):
                flag = False
                break
        if flag:
            count += 1
print(count)
