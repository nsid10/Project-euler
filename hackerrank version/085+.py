from math import ceil

box = {}
for x in range(2000, 0, -1):
    cut = ceil(((x**4 + 2 * x**3 + 32000001 * x**2 + 32000000 * x)
                ** 0.5 - x**2 - x) / (2 * (x**2 + x)))
    if cut < x:
        start = cut
    else:
        start = x
    for y in range(start, 0, -1):
        rect = x * (x + 1) * y * (y + 1) // 4
        if rect > 2001000:
            continue
        if rect in box:
            if box[rect] < x * y:
                box[rect] = x * y
        else:
            box[rect] = x * y

t = int(input())
for i in range(t):
    target = int(input())
    if target in box:
        print(box[target])
    else:
        t1, t2 = target, target
        while True:
            t1 += 1
            t2 -= 1
            if t1 in box:
                if t2 in box:
                    if box[t1] > box[t2]:
                        print(box[t1])
                        break
                    else:
                        print(box[t2])
                        break
                else:
                    print(box[t1])
                    break
            else:
                if t2 in box:
                    print(box[t2])
                    break
