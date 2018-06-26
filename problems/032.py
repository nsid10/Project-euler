def pandigital(n):
    n = str(n)
    box = []
    for i in n:
        box.append(i)
    box.sort()
    if box == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False


def identity(l):
    box = ''
    for i in l:
        box += str(i)
    return int(box)


sum = 0
pan = set()
for i in range(2, 9877):
    for j in range(2, i):
        p = i * j
        if p in pan:
            continue
        id = identity([i, j, p])
        if id > 987654321:
            break
        elif pandigital(id):
            sum += p
            pan.add(p)
            break
print(sum)
