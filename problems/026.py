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


box = [div(i) for i in range(3, 1000)]
print(box.index(max(box)) + 3)
