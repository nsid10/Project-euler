t = int(input().strip())
f0, f1, index, digits = 0, 1, 1, 1
box = [0, 1]
for x in range(t):
    n = int(input().strip())
    while True:
        if n < len(box):
            break
        digits += 1
        while True:
            f0, f1 = f1, f0 + f1
            index += 1
            if len(str(f1)) >= digits:
                break
        box.append(index)
    print(box[n])
