def pandigital(num, d):
    box = sorted([i for i in str(num)])
    if box == ['1', '2', '3', '4', '5', '6', '7', '8', '9'][:d]:
        return True
    return False


def identity(l):
    box = ''
    for i in l:
        box += str(i)
    return int(box)


N = int(input())
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
        elif pandigital(id, N):
            sum += p
            pan.add(p)
            break
print(sum)
