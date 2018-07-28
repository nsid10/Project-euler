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


box = [0, 0, 0] + [div(i) for i in range(3, 10000)]
t = int(input())
for x in range(t):
    d = int(input())
    print(box.index(max(box[:d])))
