def group(n):
    return ''.join(sorted(str(n), reverse=True))


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


n, f = 1487, 1
while n < 10000:
    n += 3 - f
    f = -f
    b, c = n + 3330, n + 3330 * 2
    box = [n, b, c]
    for x in box:
        if primality(x):
            continue
        break
    else:
        for x in range(1, len(box)):
            if group(box[x - 1]) == group(box[x]):
                continue
            break
        else:
            print(''.join(str(e) for e in box))
            break
