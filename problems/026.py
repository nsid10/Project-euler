def div(d):
    n, box, rec = 1, set(), set()
    while True:
        if n < d:
            n *= 10
            if n not in box:
                box.add(n)
            else:
                if n not in rec:
                    rec.add(n)
                else:
                    break
        else:
            n %= d
    return len(rec)


long = 0
for i in range(2, 1000):
    if div(i) > long:
        long = div(i)
        d = i
print(d)
