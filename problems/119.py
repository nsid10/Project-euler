def digitsum(num):
    return sum(int(i) for i in str(num))


box = []
for i in range(2, 100):
    for j in range(2, 10):
        p = pow(i, j)
        if digitsum(p) == i:
            box.append(p)

box.sort()
print(box[29])
