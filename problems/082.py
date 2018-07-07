def path(box):
    size = len(box)
    for x in range(1, size):
        for y in range(size):
            temp = []
            sum = 0
            for k in range(size - y):
                sum += box[y + k][x]
                temp.append(sum + box[y + k][x - 1])
            if y != 0:
                temp.append(box[y][x] + box[y - 1][x])
            box[y][x] = min(temp)
    temp = []
    for i in range(size):
        temp.append(box[i][-1])
    return min(temp)


box = open("/home/nahian/Documents/Python/p082_matrix.txt", "r")
table = box.read().split()
mat = []
for i in table:
    row = i.split(',')
    for j in range(len(row)):
        row[j] = int(row[j])
    mat.append(row)
print(path(mat))
