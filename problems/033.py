def curio(num, den):
    n = str(num)
    d = str(den)
    if int(d[1]) != 0:
        if n[1] == d[0] and (int(n[0]) / int(d[1])) == num / den:
            return True
    return False


def fraction(num, den):
    x = 2
    while x <= num:
        if num % x == 0 and den % x == 0:
            num /= x
            den /= x
            continue
        x += 1
    return int(num), int(den)


num = 1
den = 1
for i in range(10, 100):
    for j in range(10, i):
        if curio(j, i):
            num *= j
            den *= i
print(fraction(num, den))
