def div(n, d):
    box = set()
    rec = set()
    flag = False
    while True:
        if n == 0:
            break
        if n < d:
            n *= 10
            if n not in box:
                box.add(n)
            else:
                flag = True
            if flag:
                if n not in rec:
                    rec.add(n)
                else:
                    break
        else:
            num = n // d
            n = n % d
    return len(rec)


long = 0
for i in range(2, 1000):
    if div(1, i) > long:
        long = div(1, i)
        d = i
print(d)
